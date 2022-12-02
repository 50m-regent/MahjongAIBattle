#ifndef MAHJONG_PAISET_HPP
#define MAHJONG_PAISET_HPP

#include <vector>
#include <iostream>

#include "mahjong/types/pai.hpp"

namespace mahjong {
    class Paiset {
    private:
        static inline constexpr unsigned short _SHU_MASK = 0b111'1111'1111;
        static inline constexpr unsigned char _ZI_MASK   = 0b111'1111;
        static inline constexpr unsigned char _HUA_MASK  = 0b1111'1111;

        static inline unsigned long long _mask_wanzi(const Pai pai) {
            return pai & Paiset::_SHU_MASK;
        };

        static inline unsigned long long _mask_tongzi(const Pai pai) {
            return (pai >> PaiKind::Wanzi) & Paiset::_SHU_MASK;
        };

        static inline unsigned long long _mask_suozi(const Pai pai) {
            return (pai >> (PaiKind::Wanzi + PaiKind::Tongzi)) & Paiset::_SHU_MASK;
        };

        static inline unsigned _mask_zipai(const Pai pai) {
            return (pai >> (PaiKind::Wanzi + PaiKind::Tongzi + PaiKind::Suozi)) & Paiset::_ZI_MASK;
        };

        static inline unsigned _mask_huapai(const Pai pai) {
            return (pai >> (PaiKind::Wanzi + PaiKind::Tongzi + PaiKind::Suozi + PaiKind::Zipai)) & Paiset::_HUA_MASK;
        };

        unsigned long long _wanzis  = 0;
        unsigned long long _tongzis = 0;
        unsigned long long _suozis  = 0;
        unsigned _zipais            = 0;
        unsigned _huapais           = 0;

    public:
        Paiset(const std::vector<Pai> pais);

        inline constexpr unsigned long long get_wanzis() const {
            return this->_wanzis;
        }

        inline constexpr unsigned long long get_tongzis() const {
            return this->_tongzis;
        }

        inline constexpr unsigned long long get_suozis() const {
            return this->_suozis;
        }

        inline constexpr unsigned get_zipais() const {
            return this->_zipais;
        }

        inline constexpr unsigned get_huapais() const {
            return this->_huapais;
        }

        bool add_pai(const Pai pai);
        bool remove_pai(const Pai pai);

        unsigned pai_count() const;
        unsigned count_pai(const Pai pai) const;
    };

    inline std::ostream &operator<<(std::ostream &os, const Paiset pais) {
        os<<"[";
        for (Pai pai = Pai::YiWan; static_cast<bool>(pai); pai = PaiUtilities::NEXT.at(pai)) {
            unsigned char n = pais.count_pai(pai);
            while (n--) {
                os << pai << ",";
            }
        }

        return os << "]";
    }
}

#endif