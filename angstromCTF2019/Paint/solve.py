from Crypto.Util.number import *

secret = 629921607003244034334739296597900783683872903809471621783318441724296155260647861566002145401774841786965516424821133148061140507283116747339148975177513485103967011207217568924993463569559551429141756952018711071204949930416859383037306197953684591391066287527469114753495090054370608519379326915615068308557735119497576999275516623932355604742058855833591651141407379343873413310424307672368844204423176033536465560324264458606570832918771689488513626547477988015235832957445514499444921298913651835294484177694907540420778298030233425343791552742606481998105977335541679798111463675261162481691943108104757462361
pallete = 32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385521914333389668342420684974786564569494856176035326322058077805659331026192708460314150258592864177116725943603718461857357598351152301645904403697613233287231227125684710820209725157101726931323469678542580656697935045997268352998638215525166389437335543602135433229604645318478604952148193555853611059596230656

your_mix = 14317253516668543276504878316838097235650210449758621543536146016892160048656997634541093315774403078357942150970695487937570449270120625898199254439189104072891595263513437420116930684308702803055295267600790477195902538538739117809573391251939794413361184343367694928615752045687223262368136262534778688889202144260002584306527206705616186699377315031757095455954292951059462279988296369935635246644221722025457496936215039008069820514166063271894671978845634968761626636993374291118230179892722513818307254406450607168911057458141649111515924404215975886422961651958216688209696158879621701708955382424640000048217

painting = 17665922529512695488143524113273224470194093921285273353477875204196603230641896039854934719468650093602325707751566466034447988065494130102242572713515917910688574332104680867377750329904425039785453961697828887505197701127086732126907914324992806733394244034438537271953062873710421922341053639880387051921552573241651939698279628619278357238684137922164483956735128373164911380749908774512869223017256152942356111845682044048514917460601214157119487675633689081081818805777951203838578632029105960085810547586385599419736400861419214277678792284994133722491622512615732083564207280344459191773058670866354126043620

shared_mix = pow(your_mix, secret, pallete)
print(long_to_bytes(shared_mix ^ painting))