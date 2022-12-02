#include "mahjong/types/paiset.hpp"
#include "mahjong/types/pai.hpp"

using namespace mahjong;

bool Paiset::add_pai(const Pai pai) {
    assert (1 == PaiUtilities::count_bit(pai));

    unsigned long long _wanzi  = Paiset::_mask_wanzi(pai);
    unsigned long long _tongzi = Paiset::_mask_tongzi(pai);
    unsigned long long _suozi  = Paiset::_mask_suozi(pai);
    unsigned _zipai            = Paiset::_mask_zipai(pai);
    unsigned _huapai           = Paiset::_mask_huapai(pai);

    if (_wanzi) {
        while (_wanzi & this->get_wanzis()) {
            _wanzi <<= PaiKind::Wanzi;
        }
        this->_wanzis |= _wanzi;

        return _wanzi;
    } else if (_tongzi) {
        while (_tongzi & this->get_tongzis()) {
            _wanzi <<= PaiKind::Tongzi;
        }
        this->_tongzis |= _tongzi;

        return _tongzi;
    } else if (_suozi) {
        while (_suozi & this->get_suozis()) {
            _suozi <<= PaiKind::Suozi;
        }
        this->_suozis |= _suozi;

        return _suozi;
    } else if (_zipai) {
        while (_zipai & this->get_zipais()) {
            _zipai <<= PaiKind::Zipai;
        }
        this->_zipais |= _zipai;

        return _zipai;
    } else if (_huapai) {
        while (_huapai & this->get_huapais()) {
            _huapai <<= PaiKind::Huapai;
        }
        this->_huapais |= _huapai;

        return _huapai;
    }

    return false;
}

bool Paiset::remove_pai(const Pai pai) {
    assert (1 == PaiUtilities::count_bit(pai));

    unsigned long long _wanzi  = Paiset::_mask_wanzi(pai)  << (PaiKind::Wanzi * 3);
    unsigned long long _tongzi = Paiset::_mask_tongzi(pai) << (PaiKind::Tongzi * 3);
    unsigned long long _suozi  = Paiset::_mask_suozi(pai)  << (PaiKind::Suozi * 3);
    unsigned _zipai            = Paiset::_mask_zipai(pai)  << (PaiKind::Zipai * 3);
    unsigned _huapai           = Paiset::_mask_huapai(pai) << (PaiKind::Huapai * 3);

    if (_wanzi) {
        while (!(_wanzi & this->get_wanzis())) {
            _wanzi >>= PaiKind::Wanzi;
        }
        this->_wanzis &= ~_wanzi;

        return _wanzi;
    } else if (_tongzi) {
        while (!(_tongzi & this->get_tongzis())) {
            _tongzi >>= PaiKind::Tongzi;
        }
        this->_tongzis &= ~_tongzi;

        return _tongzi;
    } else if (_suozi) {
        while (!(_suozi & this->get_suozis())) {
            _suozi >>= PaiKind::Suozi;
        }
        this->_suozis &= ~_suozi;

        return _suozi;
    } else if (_zipai) {
        while (!(_zipai & this->get_zipais())) {
            _zipai >>= PaiKind::Zipai;
        }
        this->_zipais &= ~_zipai;

        return _zipai;
    } else if (_huapai) {
        while (!(_huapai & this->get_huapais())) {
            _huapai >>= PaiKind::Huapai;
        }
        this->_huapais &= ~_huapai;

        return _huapai;
    }

    return false;
}

Paiset::Paiset(const std::vector<Pai> pais) {
    for (const Pai pai: pais) {
        this->add_pai(pai);
    }
}

unsigned Paiset::pai_count() const {
    return
        PaiUtilities::count_bit(this->get_wanzis()) +
        PaiUtilities::count_bit(this->get_tongzis()) +
        PaiUtilities::count_bit(this->get_suozis()) +
        PaiUtilities::count_bit(this->get_zipais()) +
        PaiUtilities::count_bit(this->get_huapais());
}

unsigned Paiset::count_pai(const Pai pai) const {
    unsigned long long wanzi_mask  = Paiset::_mask_wanzi(pai)  | ~static_cast<unsigned long long>(this->_SHU_MASK);
    unsigned long long tongzi_mask = Paiset::_mask_tongzi(pai) | ~static_cast<unsigned long long>(this->_SHU_MASK);
    unsigned long long suozi_mask  = Paiset::_mask_suozi(pai)  | ~static_cast<unsigned long long>(this->_SHU_MASK);
    unsigned zipai_mask  = Paiset::_mask_zipai(pai)  | ~static_cast<unsigned>(this->_ZI_MASK);
    unsigned huapai_mask = Paiset::_mask_huapai(pai) | ~static_cast<unsigned>(this->_HUA_MASK);

    unsigned long long wanzis  = this->get_wanzis();
    unsigned long long tongzis = this->get_tongzis();
    unsigned long long suozis  = this->get_suozis();
    unsigned zipais  = this->get_zipais();
    unsigned huapais = this->get_huapais();

    for (unsigned char i = 0; i < 4; i++) {
        wanzis  &= wanzi_mask;
        tongzis &= tongzi_mask;
        suozis  &= suozi_mask;
        zipais  &= zipai_mask;
        huapais &= huapai_mask;

        wanzi_mask  <<= PaiKind::Wanzi;
        tongzi_mask <<= PaiKind::Tongzi;
        suozi_mask  <<= PaiKind::Suozi;
        zipai_mask  <<= PaiKind::Zipai;
        huapai_mask <<= PaiKind::Huapai;

        wanzi_mask  |= this->_SHU_MASK;
        tongzi_mask |= this->_SHU_MASK;
        suozi_mask  |= this->_SHU_MASK;
        zipai_mask  |= this->_ZI_MASK;
        huapai_mask |= this->_HUA_MASK;
    }

    return
        PaiUtilities::count_bit(wanzis) +
        PaiUtilities::count_bit(tongzis) +
        PaiUtilities::count_bit(suozis) +
        PaiUtilities::count_bit(zipais) +
        PaiUtilities::count_bit(huapais);
}