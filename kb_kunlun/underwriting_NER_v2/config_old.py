Attachments_Abdominal_BUS = """
    # Gynecological_Attachments_Abdominal_BUS_Report_Extraction_Config.yaml

attachments_information:
  conclusion: "string"            # 结论
  CDFI: "string"                  # CDFI相关信息（如适用）

  space_occupying_lesions:        # 占位病变
    - type: "string"               # 类型，例如：“肿瘤”、“结节”、“炎性病变”等
      location: "string"           # 位置，例如：“子宫体部”、“卵巢左侧”等
      synonym: "string"            # 别名，例如：“子宫肌瘤”、“良性结节”等
      echo: "string"               # 回声强弱，例如：“低回声”、“等回声”、“高回声”
      SOLSize: "float"             # 大小，单位：厘米
      SOLSizeUnit: "string"        # 单位，通常为“cm”
      feature: "string"            # 性状特征，例如：“边缘不规则”、“内部钙化”、“空洞形成”等
      number: "integer"            # 数目
      boundary: "string"           # 边界描述，例如：“清晰”、“模糊”、“不规则”等

  organs:                          # 脏器
    - organ: "string"              # 脏器名称，例如：“子宫”、“卵巢”等
      OGSize: "float"              # 脏器大小，单位：厘米
      OGSizeUnit: "string"         # 脏器大小单位，通常为“cm”
      boundary: "string"           # 脏器边界描述，例如：“清晰”、“模糊”等

  report_notes:                    # 报告附注（如适用）
    - "string"                      # 例如："建议进行进一步的超声检查"
    - "string"                      # 例如："推荐进行MRI扫描"

  external_reports:                # 外部相关报告链接列表（如适用）
    - "string"                      # 例如："http://example.com/external_report1"
    - "string"                      # 例如："http://example.com/external_report2"

  additional_documents:            # 其他补充文件链接列表（如适用）
    - "string"                      # 例如："http://example.com/doc1"
    - "string"                      # 例如："http://example.com/doc2"

  image_links:                     # 影像图像链接列表
    - "string"                      # 例如："http://example.com/image1"
    - "string"                      # 例如："http://example.com/image2"

  contrast_enhanced_images:        # 对比增强图像链接列表（如适用）
    - "string"                      # 例如："http://example.com/ce_image1"
    - "string"                      # 例如："http://example.com/ce_image2"

  MPR_images:                      # 多平面重建图像链接列表（如适用）
    - "string"                      # 例如："http://example.com/mpr_image1"
    - "string"                      # 例如："http://example.com/mpr_image2"

  reconstructed_3D_images:         # 三维重建图像链接列表（如适用）
    - "string"                      # 例如："http://example.com/3d_image1"
    - "string"                      # 例如："http://example.com/3d_image2"

"""
Bladder_Urinary_Sys_ULTRASOUND = """
    # Bladder_Urinary_Sys_ULTRASOUND_Report_Extraction_Config.yaml

report_information:
  report_id: "string"            # 报告唯一标识
  patient_id: "string"           # 患者唯一标识
  exam_date: "YYYY-MM-DD"        # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"        # 检查部位，如“泌尿系统超声”
  conclusion: "string"           # 结论
  CDFI: "string"                 # CDFI相关信息（如适用）

patient_basic_information:
  name: "string"                 # 姓名
  gender: "string"               # 性别
  age: "integer"                 # 年龄
  birth_date: "YYYY-MM-DD"       # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"             # 身高，单位：厘米
  weight_kg: "float"             # 体重，单位：公斤
  medical_record_number: "string" # 病历号
  contact_information: "string"  # 联系方式
  allergy_history: "string"      # 过敏史
  family_history: "string"       # 家族病史
  past_medical_history: "string" # 既往病史
  smoking_history: "string"      # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

organ_extraction:
  bladder:
    volume_ml: "float"                   # 膀胱容积，单位：毫升
    wall_thickness_mm: "float"           # 膀胱壁厚度，单位：毫米
    echotexture: "string"                # 膀胱回声特性，如“均匀回声”、“不均匀回声”
    presence_of_diverticula: "boolean"    # 是否存在憩室
    diverticula_count: "integer"         # 憩室数量
    diverticula_size_cm: "float"         # 憩室大小，单位：厘米
    presence_of_calculus: "boolean"       # 是否存在结石
    calculus_count: "integer"            # 结石数量
    calculus_size_cm: "float"            # 结石大小，单位：厘米
    presence_of_mass: "boolean"          # 是否存在肿块
    mass_size_cm: "float"                # 肿块大小，单位：厘米
    mass_characteristics: "string"       # 肿块特征，如“边界清晰”、“边界模糊”
    post_void_residual_volume_ml: "float" # 尿后残余量，单位：毫升
    bladder_shape: "string"               # 膀胱形态，如“规则”、“不规则”
    bladder_position: "string"            # 膀胱位置，如“位于下腹部正中”

bladder_lesions:
  masses:
    - lesion_id: "string"               # 肿块唯一标识
      location: "string"                # 肿块具体位置，如“膀胱底部”
      size_cm: "float"                  # 肿块大小，单位：厘米
      shape: "string"                   # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      boundary: "string"                # 边界描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"            # 回声特性，如“低回声”、“等回声”、“高回声”
      posterior_features: "string"     # 后方特征，如“后方声影”、“后方声像增强”、“无后方改变”
      vascularity: "string"            # 血流情况，如“血流丰富”、“血流少”、“无血流”
      suspected_diagnosis: "string"    # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"    # 其他特征描述，如“钙化”、“囊性变”等

quantitative_metrics:
  bladder_volume_ml: "float"                  # 膀胱体积，单位：毫升
  post_void_residual_volume_ml: "float"       # 尿后残余量，单位：毫升
  bladder_wall_thickness_statistics_mm: "string" # 膀胱壁厚度统计，如“平均厚度2.5mm，最大厚度3.0mm”

diagnostic_opinion:
  accurate_diagnosis: "string"                # 准确的诊断名称

comparative_study:
  compared_with_past_ultrasound: "string"     # 与既往超声影像对比描述
  change_description: "string"                # 变化描述，如“增大”、“缩小”等

report_details:
  report_generated_date: "YYYY-MM-DD"         # 报告生成日期
  report_generated_time: "HH:MM"              # 报告生成时间
  radiologist_name: "string"                  # 放射科医生姓名
  radiologist_signature: "string"             # 放射科医生签名
  report_number: "string"                     # 报告编号
  remarks: "string"                           # 备注

attachments_and_additional_info:
  image_links:                                # 影像图像链接列表
    - "string"
    - "string"
  contrast_enhanced_images:                   # 对比增强图像链接列表（如适用）
    - "string"
    - "string"
  MPR_images:                                 # 多平面重建图像链接列表（如适用）
    - "string"
    - "string"
  reconstructed_3D_images:                    # 三维重建图像链接列表（如适用）
    - "string"
    - "string"
  external_reports:                           # 外部相关报告链接列表（如适用）
    - "string"
    - "string"
  additional_documents:                       # 其他补充文件链接列表（如适用）
    - "string"
    - "string"
  report_notes:                               # 报告附注（如适用）
    - "string"
    - "string"

"""
Breast_Ultrasound = """
    # Breast_Ultrasound_Report_Extraction_Config.yaml

report_information:
  report_id: "string"            # 报告唯一标识
  patient_id: "string"           # 患者唯一标识
  exam_date: "YYYY-MM-DD"        # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"        # 检查部位，如“乳腺”
  conclusion: "string"           # 结论
  CDFI: "string"                 # CDFI相关信息（如适用）

patient_basic_information:
  name: "string"                 # 姓名
  gender: "string"               # 性别
  age: "integer"                 # 年龄
  birth_date: "YYYY-MM-DD"       # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"             # 身高，单位：厘米
  weight_kg: "float"             # 体重，单位：公斤
  medical_record_number: "string" # 病历号
  contact_information: "string"  # 联系方式
  allergy_history: "string"      # 过敏史
  family_history: "string"       # 家族病史
  past_medical_history: "string" # 既往病史
  smoking_history: "string"      # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

organ_extraction:
  breast_left:
    size_cm: "float"               # 左乳大小，单位：厘米
    echotexture: "string"          # 左乳回声特性，如“均匀回声”、“杂乱回声”等
    ducts: "string"                # 左乳导管情况，如“未见异常扩张”、“导管扩张”等
    surrounding_tissues: "string"   # 左乳周围组织描述，如“皮下脂肪组织清晰”、“未见异常”等
  breast_right:
    size_cm: "float"               # 右乳大小，单位：厘米
    echotexture: "string"          # 右乳回声特性，如“均匀回声”、“杂乱回声”等
    ducts: "string"                # 右乳导管情况，如“未见异常扩张”、“导管扩张”等
    surrounding_tissues: "string"   # 右乳周围组织描述，如“皮下脂肪组织清晰”、“未见异常”等
  skin: "string"                    # 皮肤描述，如“皮肤光滑”、“皮肤增厚”等
  nipple: "string"                  # 乳头描述，如“乳头中央对称”、“乳头溢液”等
  axillary_region: "string"         # 腋窝区描述，如“腋窝淋巴结未见异常”、“腋窝淋巴结肿大”等

breast_lesions:
  masses:
    - lesion_id: "string"           # 肿块唯一标识
      side: "string"                # 所在侧别，如“左”、“右”、“双侧”
      location: "string"            # 肿块具体位置，如“左乳上外象限”
      size_cm: "float"              # 肿块大小，单位：厘米
      shape: "string"               # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      margins: "string"             # 边缘描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"         # 回声特性，如“低回声”、“等回声”、“高回声”
      posterior_features: "string"  # 后方特征，如“后方声影”、“后方声像增强”、“无后方改变”
      vascularity: "string"         # 血流情况，如“血流丰富”、“血流少”、“无血流”
      suspected_diagnosis: "string" # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"  # 其他特征描述，如“钙化”、“囊性变”等

  cysts:
    - cyst_id: "string"             # 囊肿唯一标识
      side: "string"                # 所在侧别，如“左”、“右”、“双侧”
      location: "string"            # 囊肿具体位置，如“左乳下外象限”
      size_cm: "float"              # 囊肿大小，单位：厘米
      shape: "string"               # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      margins: "string"             # 边缘描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"         # 回声特性，如“无回声”、“低回声”、“混合回声”
      posterior_features: "string"  # 后方特征，如“后方声影”、“后方声像增强”、“无后方改变”
      vascularity: "string"         # 血流情况，如“血流丰富”、“血流少”、“无血流”
      suspected_diagnosis: "string" # 疑似诊断，如“单纯性囊肿”、“复杂囊肿”
      additional_features: "string"  # 其他特征描述，如“囊壁增厚”、“分隔”等

  other_lesions:
    - lesion_id: "string"           # 其他病变唯一标识
      type: "string"                # 病变类型，如“纤维腺瘤”、“导管内乳头状瘤”等
      side: "string"                # 所在侧别，如“左”、“右”、“双侧”
      location: "string"            # 病变具体位置，如“左乳上内象限”
      size_cm: "float"              # 病变大小，单位：厘米
      shape: "string"               # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      margins: "string"             # 边缘描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"         # 回声特性，如“低回声”、“等回声”、“高回声”
      posterior_features: "string"  # 后方特征，如“后方声影”、“后方声像增强”、“无后方改变”
      vascularity: "string"         # 血流情况，如“血流丰富”、“血流少”、“无血流”
      suspected_diagnosis: "string" # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"  # 其他特征描述，如“钙化”、“囊性变”等

lymph_nodes:
  - node_id: "string"              # 淋巴结唯一标识
    size_cm: "float"                # 淋巴结大小，单位：厘米
    location: "string"              # 位置，如“腋窝”、“锁骨上”等
    morphology: "string"            # 形态描述，如“圆形”、“卵圆形”、“结节状”等
    hilum_visibility: "string"      # 门静脉可见性，如“可见”、“不可见”
    suspicious_features: "string"   # 可疑特征，如“形态不规则”、“边缘模糊”等
    suspected_diagnosis: "string"   # 疑似诊断，如“转移性淋巴结”等

quantitative_metrics:
  breast_volume_left_ml: "float"       # 左乳体积，单位：毫升
  breast_volume_right_ml: "float"      # 右乳体积，单位：毫升
  masses_volume_statistics: "string"   # 肿块体积统计
  cysts_volume_statistics: "string"    # 囊肿体积统计
  blood_vessels_distribution: "string" # 血管分布和直径描述

diagnostic_opinion:
  accurate_diagnosis: "string"          # 准确的诊断名称

comparative_study:
  compared_with_past_ultrasound: "string" # 与既往超声影像对比描述
  change_description: "string"           # 变化描述，如“增大”、“缩小”等

report_details:
  report_generated_date: "YYYY-MM-DD"    # 报告生成日期
  report_generated_time: "HH:MM"         # 报告生成时间
  radiologist_name: "string"             # 放射科医生姓名
  radiologist_signature: "string"        # 放射科医生签名
  report_number: "string"                # 报告编号
  remarks: "string"                      # 备注

attachments_and_additional_info:
  image_links:                            # 影像图像链接列表
    - "string"
    - "string"
  contrast_enhanced_images:               # 对比增强图像链接列表（如适用）
    - "string"
    - "string"
  MPR_images:                             # 多平面重建图像链接列表（如适用）
    - "string"
    - "string"
  reconstructed_3D_images:                # 三维重建图像链接列表（如适用）
    - "string"
    - "string"

"""
Chest_Xray = """
    # Chest_Xray_Report_Extraction_Config.yaml

report_information:
  report_id: "string"                  # 报告唯一标识
  patient_id: "string"                 # 患者唯一标识
  exam_date: "YYYY-MM-DD"              # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"              # 检查部位，如“胸部X线”
  conclusion: "string"                 # 结论
  CDFI: "string"                       # CDFI相关信息（如适用，可设置为null）

patient_basic_information:
  name: "string"                       # 姓名
  gender: "string"                     # 性别
  age: "integer"                       # 年龄
  birth_date: "YYYY-MM-DD"             # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"                   # 身高，单位：厘米
  weight_kg: "float"                   # 体重，单位：公斤
  medical_record_number: "string"      # 病历号
  contact_information: "string"        # 联系方式
  allergy_history: "string"            # 过敏史
  family_history: "string"             # 家族病史
  past_medical_history: "string"       # 既往病史
  smoking_history: "string"            # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

findings:
  heart_size:
    cardiothoracic_ratio: "float"       # 心胸比，单位：%
    description: "string"               # 描述，如“正常”、“增大”等

  lungs:
    - zone: "string"                    # 肺区，如“右上肺野”、“左下肺野”等
      opacity: "string"                 # 阴影描述，如“结节性阴影”、“浸润性阴影”、“空洞”等
      size_cm: "float"                  # 阴影大小，单位：厘米
      shape: "string"                   # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      boundary: "string"                # 边界描述，如“清晰”、“模糊”、“不规则”
      associated_features: "string"     # 相关特征，如“空洞形成”、“钙化”等
      number: "integer"                  # 数目
      suspected_diagnosis: "string"      # 疑似诊断，如“良性结节”、“恶性肿瘤”等

  pleura:
    presence_of_effusion: "boolean"      # 是否存在胸腔积液
    effusion_side: "string"              # 积液侧别，如“左侧”、“右侧”、“双侧”
    effusion_volume_ml: "float"          # 积液量，单位：毫升
    effusion_characteristics: "string"   # 积液特征，如“清亮”、“复杂性”等

  bones:
    presence_of_fracture: "boolean"      # 是否存在骨折
    fracture_location: "string"          # 骨折位置，如“锁骨”、“肋骨”等
    fracture_type: "string"              # 骨折类型，如“横行骨折”、“螺旋骨折”等

  mediastinum:
    widening: "boolean"                  # 是否存在纵隔扩大
    widening_measure_cm: "float"          # 纵隔宽度，单位：厘米
    description: "string"                 # 描述，如“主动脉扩大”、“气管偏移”等

  diaphragm:
    presence_of_hernia: "boolean"        # 是否存在膈疝
    hernia_side: "string"                # 膈疝侧别，如“左侧”、“右侧”
    hernia_contents: "string"            # 膈疝内容，如“胃”、“肠道”等

quantitative_metrics:
  cardiothoracic_ratio: "float"           # 心胸比，单位：%
  lung_volume_estimation_ml: "float"      # 肺容量估计，单位：毫升
  effusion_volume_ml: "float"             # 积液量，单位：毫升
  mediastinal_width_cm: "float"           # 纵隔宽度，单位：厘米

diagnostic_opinion:
  accurate_diagnosis: "string"            # 准确的诊断名称

comparative_study:
  compared_with_past_xray: "string"       # 与既往胸片对比描述
  change_description: "string"            # 变化描述，如“增大”、“缩小”等

report_details:
  report_generated_date: "YYYY-MM-DD"     # 报告生成日期
  report_generated_time: "HH:MM"          # 报告生成时间
  radiologist_name: "string"              # 放射科医生姓名
  radiologist_signature: "string"         # 放射科医生签名
  report_number: "string"                 # 报告编号
  remarks: "string"                       # 备注

attachments_and_additional_info:
  image_links:                            # 影像图像链接列表
    - "string"                            # 例如："http://example.com/image1"
    - "string"                            # 例如："http://example.com/image2"
  contrast_enhanced_images:               # 对比增强图像链接列表（如适用）
    - "string"                            # 例如："http://example.com/ce_image1"
    - "string"                            # 例如："http://example.com/ce_image2"
  MPR_images:                             # 多平面重建图像链接列表（如适用）
    - "string"                            # 例如："http://example.com/mpr_image1"
    - "string"                            # 例如："http://example.com/mpr_image2"
  reconstructed_3D_images:                # 三维重建图像链接列表（如适用）
    - "string"                            # 例如："http://example.com/3d_image1"
    - "string"                            # 例如："http://example.com/3d_image2"
  external_reports:                       # 外部相关报告链接列表（如适用）
    - "string"                            # 例如："http://example.com/external_report1"
    - "string"                            # 例如："http://example.com/external_report2"
  additional_documents:                   # 其他补充文件链接列表（如适用）
    - "string"                            # 例如："http://example.com/doc1"
    - "string"                            # 例如："http://example.com/doc2"
  report_notes:                           # 报告附注（如适用）
    - "string"                            # 例如："建议进行进一步的CT扫描"
    - "string"                            # 例如："推荐进行MRI检查"

"""
Echocardiogram = """
    # Echocardiogram_Report_Extraction_Config.yaml

report_information:
  report_id: "string"                    # 报告唯一标识
  patient_id: "string"                   # 患者唯一标识
  exam_date: "YYYY-MM-DD"                # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"                # 检查部位，如“超声心动图”
  conclusion: "string"                   # 结论
  recommendations: "string"              # 建议（如适用）

patient_basic_information:
  name: "string"                         # 姓名
  gender: "string"                       # 性别
  age: "integer"                         # 年龄
  birth_date: "YYYY-MM-DD"               # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"                     # 身高，单位：厘米
  weight_kg: "float"                     # 体重，单位：公斤
  medical_record_number: "string"        # 病历号
  contact_information: "string"          # 联系方式
  allergy_history: "string"              # 过敏史
  family_history: "string"               # 家族病史
  past_medical_history: "string"         # 既往病史
  smoking_history: "string"              # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

echocardiogram_findings:
  chambers:
    left_atrium:
      size_cm: "float"                    # 左心房大小，单位：厘米
      size_unit: "string"                 # 单位，通常为“cm”
      volume_ml: "float"                   # 左心房容积，单位：毫升
      volume_unit: "string"                # 单位，通常为“ml”
      wall_thickness_mm: "float"           # 左心房壁厚，单位：毫米
      wall_thickness_unit: "string"        # 单位，通常为“mm”
      function: "string"                   # 功能描述，如“正常”、“扩大”等

    left_ventricle:
      size_cm: "float"                    # 左心室大小，单位：厘米
      size_unit: "string"                 # 单位，通常为“cm”
      volume_ml: "float"                   # 左心室容积，单位：毫升
      volume_unit: "string"                # 单位，通常为“ml”
      wall_thickness_mm: "float"           # 左心室壁厚，单位：毫米
      wall_thickness_unit: "string"        # 单位，通常为“mm”
      ejection_fraction_percent: "float"    # 射血分数，单位：%
      fractional_shortening_percent: "float" # 短缩分数，单位：%
      function: "string"                   # 功能描述，如“正常”、“收缩功能减退”等

    right_atrium:
      size_cm: "float"                    # 右心房大小，单位：厘米
      size_unit: "string"                 # 单位，通常为“cm”
      volume_ml: "float"                   # 右心房容积，单位：毫升
      volume_unit: "string"                # 单位，通常为“ml”
      wall_thickness_mm: "float"           # 右心房壁厚，单位：毫米
      wall_thickness_unit: "string"        # 单位，通常为“mm”
      function: "string"                   # 功能描述，如“正常”、“扩大”等

    right_ventricle:
      size_cm: "float"                    # 右心室大小，单位：厘米
      size_unit: "string"                 # 单位，通常为“cm”
      volume_ml: "float"                   # 右心室容积，单位：毫升
      volume_unit: "string"                # 单位，通常为“ml”
      wall_thickness_mm: "float"           # 右心室壁厚，单位：毫米
      wall_thickness_unit: "string"        # 单位，通常为“mm”
      function: "string"                   # 功能描述，如“正常”、“收缩功能减退”等

  valves:
    mitral_valve:
      morphology: "string"                  # 形态，如“正常”、“瓣膜增厚”等
      regurgitation_grade: "integer"        # 返流分级，如1-4级
      stenosis_grade: "integer"             # 狭窄分级，如1-4级
      associated_features: "string"         # 相关特征，如“钙化”、“脱垂”等

    aortic_valve:
      morphology: "string"                  # 形态，如“正常”、“瓣膜增厚”等
      regurgitation_grade: "integer"        # 返流分级，如1-4级
      stenosis_grade: "integer"             # 狭窄分级，如1-4级
      associated_features: "string"         # 相关特征，如“钙化”、“脱垂”等

    tricuspid_valve:
      morphology: "string"                  # 形态，如“正常”、“瓣膜增厚”等
      regurgitation_grade: "integer"        # 返流分级，如1-4级
      stenosis_grade: "integer"             # 狭窄分级，如1-4级
      associated_features: "string"         # 相关特征，如“钙化”、“脱垂”等

    pulmonary_valve:
      morphology: "string"                  # 形态，如“正常”、“瓣膜增厚”等
      regurgitation_grade: "integer"        # 返流分级，如1-4级
      stenosis_grade: "integer"             # 狭窄分级，如1-4级
      associated_features: "string"         # 相关特征，如“钙化”、“脱垂”等

  pericardium:
    effusion_present: "boolean"             # 是否存在心包积液
    effusion_volume_ml: "float"             # 心包积液量，单位：毫升
    effusion_characteristics: "string"      # 心包积液特征，如“无”、“少量”、“中量”、“大量”
    constrictive_pericarditis: "boolean"    # 是否存在限制性心包炎

  wall_motion:
    abnormalities_present: "boolean"        # 是否存在壁运动异常
    regions_with_abnormal_motion: "list"    # 存在壁运动异常的区域，如“前壁”、“侧壁”等
    description: "string"                   # 描述，如“运动减弱”、“运动缺失”等

  doppler_findings:
    mitral_inflow:
      e_velocity_cm_s: "float"              # E波速度，单位：cm/s
      a_velocity_cm_s: "float"              # A波速度，单位：cm/s
      e_a_ratio: "float"                     # E/A比值
      deceleration_time_ms: "float"          # E波减速时间，单位：毫秒

    tricuspid_inflow:
      e_velocity_cm_s: "float"              # E波速度，单位：cm/s
      a_velocity_cm_s: "float"              # A波速度，单位：cm/s
      e_a_ratio: "float"                     # E/A比值
      deceleration_time_ms: "float"          # E波减速时间，单位：毫秒

    aortic_outflow:
      velocity_cm_s: "float"                # 最高速度，单位：cm/s
      pressure_gradient_mmHg: "float"        # 压力梯度，单位：mmHg

    pulmonic_outflow:
      velocity_cm_s: "float"                # 最高速度，单位：cm/s
      pressure_gradient_mmHg: "float"        # 压力梯度，单位：mmHg

quantitative_metrics:
  ejection_fraction_percent: "float"          # 射血分数，单位：%
  fractional_shortening_percent: "float"      # 短缩分数，单位：%
  left_atrium_volume_ml: "float"               # 左心房容积，单位：毫升
  left_ventricle_volume_ml: "float"            # 左心室容积，单位：毫升
  right_atrium_volume_ml: "float"              # 右心房容积，单位：毫升
  right_ventricle_volume_ml: "float"           # 右心室容积，单位：毫升
  mitral_valve_area_cm2: "float"               # 二尖瓣面积，单位：cm²
  aortic_valve_area_cm2: "float"               # 主动脉瓣面积，单位：cm²
  tricuspid_valve_area_cm2: "float"            # 三尖瓣面积，单位：cm²
  pulmonary_valve_area_cm2: "float"            # 肺动脉瓣面积，单位：cm²

diagnostic_opinion:
  accurate_diagnosis: "string"                  # 准确的诊断名称

comparative_study:
  compared_with_past_ecg: "string"              # 与既往心电图对比描述
  change_description: "string"                  # 变化描述，如“增大”、“缩小”等

report_details:
  report_generated_date: "YYYY-MM-DD"           # 报告生成日期
  report_generated_time: "HH:MM"                # 报告生成时间
  cardiologist_name: "string"                   # 心脏病专科医生姓名
  cardiologist_signature: "string"              # 心脏病专科医生签名
  report_number: "string"                       # 报告编号
  remarks: "string"                             # 备注

attachments_and_additional_info:
  image_links:                                  # 影像图像链接列表
    - "string"                                  # 例如："http://example.com/ecg_image1"
    - "string"                                  # 例如："http://example.com/ecg_image2"
  external_reports:                             # 外部相关报告链接列表（如适用）
    - "string"                                  # 例如："http://exam

"""
Gallbladder_Abdominal_BUS = """
    # Gallbladder_Abdominal_BUS_Report_Extraction_Config.yaml

report_information:
  report_id: "string"            # 报告唯一标识
  patient_id: "string"           # 患者唯一标识
  exam_date: "YYYY-MM-DD"        # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"        # 检查部位，如“腹部B超”
  conclusion: "string"           # 结论
  CDFI: "string"                 # CDFI相关信息（如适用）

patient_basic_information:
  name: "string"                 # 姓名
  gender: "string"               # 性别
  age: "integer"                 # 年龄
  birth_date: "YYYY-MM-DD"       # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"             # 身高，单位：厘米
  weight_kg: "float"             # 体重，单位：公斤
  medical_record_number: "string" # 病历号
  contact_information: "string"  # 联系方式
  allergy_history: "string"      # 过敏史
  family_history: "string"       # 家族病史
  past_medical_history: "string" # 既往病史
  smoking_history: "string"      # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

organ_extraction:
  gallbladder:
    size_length_cm: "float"          # 胆囊长度，单位：厘米
    size_width_cm: "float"           # 胆囊宽度，单位：厘米
    wall_thickness_cm: "float"       # 胆囊壁厚度，单位：厘米
    wall_echogenicity: "string"      # 胆囊壁回声特性，如“均匀回声”、“高回声”等
    wall_surface: "string"           # 胆囊壁表面描述，如“光滑”、“不规则”等
    pericholecystic_fluid: "string"   # 胆囊周围液体，如“无”、“少量”、“大量”等
    gallstones_present: "boolean"    # 是否存在胆结石
    gallstones_count: "integer"      # 胆结石数量
    gallstones_size_cm: "float"      # 胆结石大小，单位：厘米
    polyps_present: "boolean"        # 是否存在胆囊息肉
    polyps_count: "integer"          # 胆囊息肉数量
    polyps_size_cm: "float"          # 胆囊息肉大小，单位：厘米
    sludge_present: "boolean"        # 是否存在胆泥
    sludge_description: "string"     # 胆泥描述，如“少量”、“中量”、“大量”等
    sonographic_murphy_sign: "string" # 超声Murphy征，如“阳性”、“阴性”
    adjacent_organs: "string"         # 邻近器官描述，如“肝脏形态正常”

gallbladder_lesions:
  masses:
    - lesion_id: "string"             # 肿块唯一标识
      side: "string"                  # 所在侧别，如“左”、“右”、“双侧” (胆囊通常无侧别，可省略)
      location: "string"              # 肿块具体位置，如“胆囊体部”
      size_cm: "float"                # 肿块大小，单位：厘米
      shape: "string"                 # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      margins: "string"               # 边缘描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"           # 回声特性，如“低回声”、“等回声”、“高回声”
      posterior_features: "string"    # 后方特征，如“后方声影”、“后方声像增强”、“无后方改变”
      vascularity: "string"           # 血流情况，如“血流丰富”、“血流少”、“无血流”
      suspected_diagnosis: "string"   # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"   # 其他特征描述，如“钙化”、“囊性变”等

  polyps:
    - polyp_id: "string"              # 息肉唯一标识
      location: "string"               # 息肉具体位置，如“胆囊颈部”
      size_cm: "float"                 # 息肉大小，单位：厘米
      echogenicity: "string"            # 回声特性，如“低回声”、“等回声”、“高回声”
      margins: "string"                 # 边缘描述，如“光滑”、“不规则”
      suspected_diagnosis: "string"     # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"     # 其他特征描述，如“钙化”、“囊性变”等

  other_lesions:
    - lesion_id: "string"             # 其他病变唯一标识
      type: "string"                  # 病变类型，如“腺瘤”、“炎性病变”等
      location: "string"              # 病变具体位置，如“胆囊体部”
      size_cm: "float"                # 病变大小，单位：厘米
      shape: "string"                 # 形态描述，如“不规则形”、“结节状”等
      margins: "string"               # 边缘描述，如“模糊”、“分叶”等
      echogenicity: "string"           # 回声特性，如“高回声”、“等回声”等
      posterior_features: "string"    # 后方特征，如“后方声像增强”
      vascularity: "string"           # 血流情况，如“少”、“无血流”
      suspected_diagnosis: "string"   # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"   # 其他特征描述，如“钙化”、“空洞形成”等

lymph_nodes:
  - node_id: "string"                  # 淋巴结唯一标识
    size_cm: "float"                    # 淋巴结大小，单位：厘米
    location: "string"                  # 位置，如“肝门旁”、“腹主动脉旁”等
    morphology: "string"                # 形态描述，如“圆形”、“卵圆形”等
    hilum_visibility: "string"          # 门静脉可见性，如“可见”、“不可见”
    suspicious_features: "string"       # 可疑特征，如“形态不规则”、“边缘模糊”等
    suspected_diagnosis: "string"       # 疑似诊断，如“转移性淋巴结”等

quantitative_metrics:
  gallbladder_volume_ml: "float"         # 胆囊体积，单位：毫升
  lesions_volume_statistics: "string"     # 病变体积统计
  blood_vessels_distribution: "string"    # 血管分布和直径描述

diagnostic_opinion:
  accurate_diagnosis: "string"            # 准确的诊断名称

comparative_study:
  compared_with_past_ultrasound: "string" # 与既往超声影像对比描述
  change_description: "string"            # 变化描述，如“增大”、“缩小”等

report_details:
  report_generated_date: "YYYY-MM-DD"     # 报告生成日期
  report_generated_time: "HH:MM"          # 报告生成时间
  radiologist_name: "string"              # 放射科医生姓名
  radiologist_signature: "string"         # 放射科医生签名
  report_number: "string"                 # 报告编号
  remarks: "string"                       # 备注

attachments_and_additional_info:
  image_links:                            # 影像图像链接列表
    - "string"
    - "string"
  contrast_enhanced_images:               # 对比增强图像链接列表（如适用）
    - "string"
    - "string"
  MPR_images:                             # 多平面重建图像链接列表（如适用）
    - "string"
    - "string"
  reconstructed_3D_images:                # 三维重建图像链接列表（如适用）
    - "string"
    - "string"

"""
Holter_ECG = """
    # Holter_ECG_Report_Extraction_Config.yaml

report_information:
  report_id: "string"                  # 报告唯一标识
  patient_id: "string"                 # 患者唯一标识
  exam_start_date: "YYYY-MM-DD"        # 检查开始日期，格式：YYYY-MM-DD
  exam_start_time: "HH:MM"             # 检查开始时间，格式：HH:MM
  exam_end_date: "YYYY-MM-DD"          # 检查结束日期，格式：YYYY-MM-DD
  exam_end_time: "HH:MM"               # 检查结束时间，格式：HH:MM
  exam_location: "string"              # 检查部位，如“动态心电图”
  conclusion: "string"                 # 结论
  recommendations: "string"            # 建议（如适用）

patient_basic_information:
  name: "string"                       # 姓名
  gender: "string"                     # 性别
  age: "integer"                       # 年龄
  birth_date: "YYYY-MM-DD"             # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"                   # 身高，单位：厘米
  weight_kg: "float"                   # 体重，单位：公斤
  medical_record_number: "string"      # 病历号
  contact_information: "string"        # 联系方式
  allergy_history: "string"            # 过敏史
  family_history: "string"             # 家族病史
  past_medical_history: "string"       # 既往病史
  smoking_history: "string"            # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

ECG_findings:
  average_heart_rate_bpm: "integer"     # 平均心率，单位：次/分钟
  minimum_heart_rate_bpm: "integer"     # 最低心率，单位：次/分钟
  maximum_heart_rate_bpm: "integer"     # 最高心率，单位：次/分钟
  heart_rate_variability: "string"       # 心率变异性，如“正常”、“降低”、“增加”
  rhythm: "string"                       # 心律，如“窦性心律”、“房颤”、“室性早搏”等
  episodes_of_arrhythmia:               # 心律失常发作
    - episode_id: "string"               # 发作唯一标识
      type: "string"                      # 发作类型，如“房性早搏”、“室性早搏”、“房颤”等
      start_time: "HH:MM"                 # 发作开始时间，格式：HH:MM
      end_time: "HH:MM"                   # 发作结束时间，格式：HH:MM
      duration_seconds: "integer"         # 发作持续时间，单位：秒
      heart_rate_bpm: "integer"            # 发作期间心率，单位：次/分钟
      associated_features: "string"       # 相关特征，如“心悸”、“胸痛”等

quantitative_metrics:
  total_monitoring_duration_hours: "float"  # 总监测时长，单位：小时
  total_episodes_of_arrhythmia: "integer"   # 心律失常发作总数
  average_heart_rate_bpm: "integer"          # 平均心率，单位：次/分钟
  minimum_heart_rate_bpm: "integer"          # 最低心率，单位：次/分钟
  maximum_heart_rate_bpm: "integer"          # 最高心率，单位：次/分钟
  heart_rate_variability_index: "float"      # 心率变异性指数

diagnostic_opinion:
  accurate_diagnosis: "string"                # 准确的诊断名称

comparative_study:
  compared_with_past_ecg: "string"            # 与既往心电图对比描述
  change_description: "string"                # 变化描述，如“心律失常发作增多”、“心率变异性降低”等

report_details:
  report_generated_date: "YYYY-MM-DD"         # 报告生成日期
  report_generated_time: "HH:MM"              # 报告生成时间
  cardiologist_name: "string"                 # 心脏病专科医生姓名
  cardiologist_signature: "string"            # 心脏病专科医生签名
  report_number: "string"                     # 报告编号
  remarks: "string"                           # 备注

attachments_and_additional_info:
  image_links:                                # 影像图像链接列表
    - "string"                                # 例如："http://example.com/ecg_image1"
    - "string"                                # 例如："http://example.com/ecg_image2"
  external_reports:                           # 外部相关报告链接列表（如适用）
    - "string"                                # 例如："http://example.com/external_report1"
    - "string"                                # 例如："http://example.com/external_report2"
  additional_documents:                       # 其他补充文件链接列表（如适用）
    - "string"                                # 例如："http://example.com/doc1"
    - "string"                                # 例如："http://example.com/doc2"
  report_notes:                               # 报告附注（如适用）
    - "string"                                # 例如："建议进行心脏超声检查"
    - "string"                                # 例如："推荐进行血液检查"

"""
Kidney_Abdominal_BUS = """
    # Kidney_Abdominal_BUS_Report_Extraction_Config.yaml

report_information:
  report_id: "string"            # 报告唯一标识
  patient_id: "string"           # 患者唯一标识
  exam_date: "YYYY-MM-DD"        # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"        # 检查部位，如“腹部B超”
  conclusion: "string"           # 结论
  CDFI: "string"                 # CDFI相关信息（如适用）

patient_basic_information:
  name: "string"                 # 姓名
  gender: "string"               # 性别
  age: "integer"                 # 年龄
  birth_date: "YYYY-MM-DD"       # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"             # 身高，单位：厘米
  weight_kg: "float"             # 体重，单位：公斤
  medical_record_number: "string" # 病历号
  contact_information: "string"  # 联系方式
  allergy_history: "string"      # 过敏史
  family_history: "string"       # 家族病史
  past_medical_history: "string" # 既往病史
  smoking_history: "string"      # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

organ_extraction:
  kidney_left:
    size_length_cm: "float"          # 左肾长度，单位：厘米
    size_width_cm: "float"           # 左肾宽度，单位：厘米
    size_thickness_cm: "float"       # 左肾厚度，单位：厘米
    echotexture: "string"            # 左肾回声特性，如“均匀回声”、“杂乱回声”等
    borders: "string"                # 左肾边界描述，如“清晰”、“模糊”等
    renal_pelvis_size_cm: "float"    # 左肾肾盂大小，单位：厘米
    hydronephrosis_degree: "string"  # 左肾积水程度，如“无”、“轻度”、“中度”、“重度”
    perirenal_fat: "string"          # 左肾周围脂肪描述，如“未见积液”、“少量积液”等
    cortical_thickness_cm: "float"    # 左肾皮质厚度，单位：厘米
    medullary_echo: "string"         # 左肾髓质回声，如“正常”、“低回声”等
    adjacent_organs: "string"        # 邻近器官描述，如“脾脏形态正常”
  
  kidney_right:
    size_length_cm: "float"          # 右肾长度，单位：厘米
    size_width_cm: "float"           # 右肾宽度，单位：厘米
    size_thickness_cm: "float"       # 右肾厚度，单位：厘米
    echotexture: "string"            # 右肾回声特性，如“均匀回声”、“杂乱回声”等
    borders: "string"                # 右肾边界描述，如“清晰”、“模糊”等
    renal_pelvis_size_cm: "float"    # 右肾肾盂大小，单位：厘米
    hydronephrosis_degree: "string"  # 右肾积水程度，如“无”、“轻度”、“中度”、“重度”
    perirenal_fat: "string"          # 右肾周围脂肪描述，如“未见积液”、“少量积液”等
    cortical_thickness_cm: "float"    # 右肾皮质厚度，单位：厘米
    medullary_echo: "string"         # 右肾髓质回声，如“正常”、“低回声”等
    adjacent_organs: "string"        # 邻近器官描述，如“肝脏形态正常”

kidney_lesions:
  masses:
    - lesion_id: "string"             # 肿块唯一标识
      side: "string"                  # 所在侧别，如“左”、“右”、“双侧”
      location: "string"              # 肿块具体位置，如“肾上极”、“肾中极”、“肾下极”
      size_cm: "float"                # 肿块大小，单位：厘米
      shape: "string"                 # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      margins: "string"               # 边缘描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"           # 回声特性，如“低回声”、“等回声”、“高回声”
      posterior_features: "string"    # 后方特征，如“后方声影”、“后方声像增强”、“无后方改变”
      vascularity: "string"           # 血流情况，如“血流丰富”、“血流少”、“无血流”
      suspected_diagnosis: "string"   # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"   # 其他特征描述，如“钙化”、“囊性变”等

  cysts:
    - cyst_id: "string"               # 囊肿唯一标识
      side: "string"                  # 所在侧别，如“左”、“右”、“双侧”
      location: "string"              # 囊肿具体位置，如“肾上极”、“肾中极”、“肾下极”
      size_cm: "float"                # 囊肿大小，单位：厘米
      shape: "string"                 # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      margins: "string"               # 边缘描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"           # 回声特性，如“无回声”、“低回声”、“混合回声”
      posterior_features: "string"    # 后方特征，如“无后方改变”、“后方声影”
      vascularity: "string"           # 血流情况，如“无血流”
      suspected_diagnosis: "string"   # 疑似诊断，如“单纯性囊肿”、“复杂囊肿”
      additional_features: "string"   # 其他特征描述，如“囊壁增厚”、“分隔”等

  other_lesions:
    - lesion_id: "string"             # 其他病变唯一标识
      type: "string"                  # 病变类型，如“肾血管瘤”、“肾癌”等
      side: "string"                  # 所在侧别，如“左”、“右”、“双侧”
      location: "string"              # 病变具体位置，如“肾门”、“肾实质”等
      size_cm: "float"                # 病变大小，单位：厘米
      shape: "string"                 # 形态描述，如“不规则形”、“结节状”等
      margins: "string"               # 边缘描述，如“模糊”、“分叶”等
      echogenicity: "string"           # 回声特性，如“高回声”、“等回声”等
      posterior_features: "string"    # 后方特征，如“后方声影”、“后方声像增强”
      vascularity: "string"           # 血流情况，如“少”、“无血流”
      suspected_diagnosis: "string"   # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"   # 其他特征描述，如“钙化”、“空洞形成”等

lymph_nodes:
  - node_id: "string"                  # 淋巴结唯一标识
    size_cm: "float"                    # 淋巴结大小，单位：厘米
    location: "string"                  # 位置，如“肾门旁”、“腹主动脉旁”等
    morphology: "string"                # 形态描述，如“圆形”、“卵圆形”、“结节状”等
    hilum_visibility: "string"          # 门静脉可见性，如“可见”、“不可见”
    suspicious_features: "string"       # 可疑特征，如“形态不规则”、“边缘模糊”等
    suspected_diagnosis: "string"       # 疑似诊断，如“转移性淋巴结”等

quantitative_metrics:
  kidney_left_volume_ml: "float"          # 左肾体积，单位：毫升
  kidney_right_volume_ml: "float"         # 右肾体积，单位：毫升
  lesions_volume_statistics: "string"     # 结节体积统计
  blood_vessels_distribution: "string"    # 血管分布和直径描述

diagnostic_opinion:
  accurate_diagnosis: "string"            # 准确的诊断名称

comparative_study:
  compared_with_past_ultrasound: "string" # 与既往超声影像对比描述
  change_description: "string"            # 变化描述，如“增大”、“缩小”等

report_details:
  report_generated_date: "YYYY-MM-DD"     # 报告生成日期
  report_generated_time: "HH:MM"          # 报告生成时间
  radiologist_name: "string"              # 放射科医生姓名
  radiologist_signature: "string"         # 放射科医生签名
  report_number: "string"                 # 报告编号
  remarks: "string"                       # 备注

attachments_and_additional_info:
  image_links:                            # 影像图像链接列表
    - "string"
    - "string"
  contrast_enhanced_images:               # 对比增强图像链接列表（如适用）
    - "string"
    - "string"
  MPR_images:                             # 多平面重建图像链接列表（如适用）
    - "string"
    - "string"
  reconstructed_3D_images:                # 三维重建图像链接列表（如适用）
    - "string"
    - "string"

"""
Liver_Abdominal_BUS = """
    # Liver_Abdominal_BUS_Report_Extraction_Config.yaml

report_information:
  report_id: "string"            # 报告唯一标识
  patient_id: "string"           # 患者唯一标识
  exam_date: "YYYY-MM-DD"        # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"        # 检查部位，如“腹部B超”
  conclusion: "string"           # 结论
  CDFI: "string"                 # CDFI相关信息（如适用）

patient_basic_information:
  name: "string"                 # 姓名
  gender: "string"               # 性别
  age: "integer"                 # 年龄
  birth_date: "YYYY-MM-DD"       # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"             # 身高，单位：厘米
  weight_kg: "float"             # 体重，单位：公斤
  medical_record_number: "string" # 病历号
  contact_information: "string"  # 联系方式
  allergy_history: "string"      # 过敏史
  family_history: "string"       # 家族病史
  past_medical_history: "string" # 既往病史
  smoking_history: "string"      # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

organ_extraction:
  liver:
    size_length_cm: "float"          # 肝脏长度，单位：厘米
    size_width_cm: "float"           # 肝脏宽度，单位：厘米
    size_thickness_cm: "float"       # 肝脏厚度，单位：厘米
    echotexture: "string"            # 肝脏回声特性，如“均匀回声”、“杂乱回声”等
    surface: "string"                # 肝脏表面描述，如“光滑”、“不规则”等
    vascular_structures: "string"     # 血管结构描述，如“门静脉形态正常”
    biliary_ducts: "string"           # 胆道描述，如“胆管未见扩张”
    adjacent_organs: "string"         # 邻近器官描述，如“胰腺形态正常”
    surrounding_tissues: "string"     # 周围组织描述，如“未见肿块”等

liver_lesions:
  masses:
    - lesion_id: "string"             # 肿块唯一标识
      side: "string"                  # 所在侧别，如“左”、“右”、“双侧”
      location: "string"              # 肿块具体位置，如“肝右叶上段”
      size_cm: "float"                # 肿块大小，单位：厘米
      shape: "string"                 # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      margins: "string"               # 边缘描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"           # 回声特性，如“低回声”、“等回声”、“高回声”
      posterior_features: "string"    # 后方特征，如“后方声影”、“后方声像增强”、“无后方改变”
      vascularity: "string"           # 血流情况，如“血流丰富”、“血流少”、“无血流”
      suspected_diagnosis: "string"   # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"   # 其他特征描述，如“钙化”、“囊性变”等

  cysts:
    - cyst_id: "string"               # 囊肿唯一标识
      side: "string"                  # 所在侧别，如“左”、“右”、“双侧”
      location: "string"              # 囊肿具体位置，如“肝左叶中段”
      size_cm: "float"                # 囊肿大小，单位：厘米
      shape: "string"                 # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      margins: "string"               # 边缘描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"           # 回声特性，如“无回声”、“低回声”、“混合回声”
      posterior_features: "string"    # 后方特征，如“无后方改变”、“后方声影”
      vascularity: "string"           # 血流情况，如“无血流”
      suspected_diagnosis: "string"   # 疑似诊断，如“单纯性囊肿”、“复杂囊肿”
      additional_features: "string"   # 其他特征描述，如“囊壁增厚”、“分隔”等

  other_lesions:
    - lesion_id: "string"             # 其他病变唯一标识
      type: "string"                  # 病变类型，如“血管瘤”、“炎性肉芽肿”等
      side: "string"                  # 所在侧别，如“左”、“右”、“双侧”
      location: "string"              # 病变具体位置，如“肝左叶下段”
      size_cm: "float"                # 病变大小，单位：厘米
      shape: "string"                 # 形态描述，如“不规则形”、“结节状”等
      margins: "string"               # 边缘描述，如“模糊”、“分叶”等
      echogenicity: "string"           # 回声特性，如“高回声”、“等回声”等
      posterior_features: "string"    # 后方特征，如“后方声影”、“后方声像增强”
      vascularity: "string"           # 血流情况，如“少”、“无血流”
      suspected_diagnosis: "string"   # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"   # 其他特征描述，如“钙化”、“空洞形成”等

lymph_nodes:
  - node_id: "string"                  # 淋巴结唯一标识
    size_cm: "float"                    # 淋巴结大小，单位：厘米
    location: "string"                  # 位置，如“肝门”、“腹主动脉旁”等
    morphology: "string"                # 形态描述，如“圆形”、“卵圆形”等
    hilum_visibility: "string"          # 门静脉可见性，如“可见”、“不可见”
    suspicious_features: "string"       # 可疑特征，如“形态不规则”、“边缘模糊”等
    suspected_diagnosis: "string"       # 疑似诊断，如“转移性淋巴结”等

quantitative_metrics:
  liver_volume_ml: "float"               # 肝脏体积，单位：毫升
  nodules_volume_statistics: "string"     # 结节体积统计
  blood_vessels_distribution: "string"    # 血管分布和直径描述

diagnostic_opinion:
  accurate_diagnosis: "string"            # 准确的诊断名称

comparative_study:
  compared_with_past_ultrasound: "string" # 与既往超声影像对比描述
  change_description: "string"            # 变化描述，如“增大”、“缩小”等

report_details:
  report_generated_date: "YYYY-MM-DD"     # 报告生成日期
  report_generated_time: "HH:MM"          # 报告生成时间
  radiologist_name: "string"              # 放射科医生姓名
  radiologist_signature: "string"         # 放射科医生签名
  report_number: "string"                 # 报告编号
  remarks: "string"                       # 备注

attachments_and_additional_info:
  image_links:                            # 影像图像链接列表
    - "string"
    - "string"
  contrast_enhanced_images:               # 对比增强图像链接列表（如适用）
    - "string"
    - "string"
  MPR_images:                             # 多平面重建图像链接列表（如适用）
    - "string"
    - "string"
  reconstructed_3D_images:                # 三维重建图像链接列表（如适用）
    - "string"
    - "string"

"""
Pancreas_Abdominal_BUS = """
    # Pancreas_Abdominal_BUS_Report_Extraction_Config.yaml

report_information:
  report_id: "string"            # 报告唯一标识
  patient_id: "string"           # 患者唯一标识
  exam_date: "YYYY-MM-DD"        # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"        # 检查部位，如“腹部B超”
  conclusion: "string"           # 结论
  CDFI: "string"                 # CDFI相关信息（如适用）

patient_basic_information:
  name: "string"                 # 姓名
  gender: "string"               # 性别
  age: "integer"                 # 年龄
  birth_date: "YYYY-MM-DD"       # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"             # 身高，单位：厘米
  weight_kg: "float"             # 体重，单位：公斤
  medical_record_number: "string" # 病历号
  contact_information: "string"  # 联系方式
  allergy_history: "string"      # 过敏史
  family_history: "string"       # 家族病史
  past_medical_history: "string" # 既往病史
  smoking_history: "string"      # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

organ_extraction:
  pancreas:
    size_length_cm: "float"          # 胰腺长度，单位：厘米
    size_width_cm: "float"           # 胰腺宽度，单位：厘米
    size_thickness_cm: "float"       # 胰腺厚度，单位：厘米
    echotexture: "string"            # 胰腺回声特性，如“均匀回声”、“杂乱回声”等
    borders: "string"                # 胰腺边界描述，如“清晰”、“模糊”等
    duct_visibility: "string"        # 胰管可见性，如“可见”、“不可见”
    main_pancreatic_duct: "string"   # 主胰管情况，如“未见扩张”、“轻度扩张”等
    surrounding_tissues: "string"     # 周围组织描述，如“未见肿块”等
    adjacent_organs: "string"         # 邻近器官描述，如“脾脏形态正常”

pancreas_lesions:
  masses:
    - lesion_id: "string"             # 肿块唯一标识
      location: "string"              # 肿块具体位置，如“胰头”、“胰体”、“胰尾”
      size_cm: "float"                # 肿块大小，单位：厘米
      shape: "string"                 # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      margins: "string"               # 边缘描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"           # 回声特性，如“低回声”、“等回声”、“高回声”
      posterior_features: "string"    # 后方特征，如“后方声影”、“后方声像增强”、“无后方改变”
      vascularity: "string"           # 血流情况，如“血流丰富”、“血流少”、“无血流”
      suspected_diagnosis: "string"   # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"   # 其他特征描述，如“钙化”、“囊性变”等

  cysts:
    - cyst_id: "string"               # 囊肿唯一标识
      location: "string"              # 囊肿具体位置，如“胰头部”、“胰体部”、“胰尾部”
      size_cm: "float"                # 囊肿大小，单位：厘米
      shape: "string"                 # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      margins: "string"               # 边缘描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"           # 回声特性，如“无回声”、“低回声”、“混合回声”
      posterior_features: "string"    # 后方特征，如“无后方改变”、“后方声影”
      vascularity: "string"           # 血流情况，如“无血流”
      suspected_diagnosis: "string"   # 疑似诊断，如“单纯性囊肿”、“复杂囊肿”
      additional_features: "string"   # 其他特征描述，如“囊壁增厚”、“分隔”等

  other_lesions:
    - lesion_id: "string"             # 其他病变唯一标识
      type: "string"                  # 病变类型，如“胰腺炎性假性囊肿”、“血管瘤”等
      location: "string"              # 病变具体位置，如“胰头部”
      size_cm: "float"                # 病变大小，单位：厘米
      shape: "string"                 # 形态描述，如“不规则形”、“结节状”等
      margins: "string"               # 边缘描述，如“模糊”、“分叶”等
      echogenicity: "string"           # 回声特性，如“高回声”、“等回声”等
      posterior_features: "string"    # 后方特征，如“后方声影”、“后方声像增强”
      vascularity: "string"           # 血流情况，如“少”、“无血流”
      suspected_diagnosis: "string"   # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"   # 其他特征描述，如“钙化”、“空洞形成”等

lymph_nodes:
  - node_id: "string"                  # 淋巴结唯一标识
    size_cm: "float"                    # 淋巴结大小，单位：厘米
    location: "string"                  # 位置，如“腹主动脉旁”、“肝门”等
    morphology: "string"                # 形态描述，如“圆形”、“卵圆形”、“结节状”等
    hilum_visibility: "string"          # 门静脉可见性，如“可见”、“不可见”
    suspicious_features: "string"       # 可疑特征，如“形态不规则”、“边缘模糊”等
    suspected_diagnosis: "string"       # 疑似诊断，如“转移性淋巴结”等

quantitative_metrics:
  pancreas_volume_ml: "float"            # 胰腺体积，单位：毫升
  nodules_volume_statistics: "string"     # 结节体积统计
  blood_vessels_distribution: "string"    # 血管分布和直径描述

diagnostic_opinion:
  accurate_diagnosis: "string"            # 准确的诊断名称

comparative_study:
  compared_with_past_ultrasound: "string" # 与既往超声影像对比描述
  change_description: "string"            # 变化描述，如“增大”、“缩小”等

report_details:
  report_generated_date: "YYYY-MM-DD"     # 报告生成日期
  report_generated_time: "HH:MM"          # 报告生成时间
  radiologist_name: "string"              # 放射科医生姓名
  radiologist_signature: "string"         # 放射科医生签名
  report_number: "string"                 # 报告编号
  remarks: "string"                       # 备注

attachments_and_additional_info:
  image_links:                            # 影像图像链接列表
    - "string"
    - "string"
  contrast_enhanced_images:               # 对比增强图像链接列表（如适用）
    - "string"
    - "string"
  MPR_images:                             # 多平面重建图像链接列表（如适用）
    - "string"
    - "string"
  reconstructed_3D_images:                # 三维重建图像链接列表（如适用）
    - "string"
    - "string"

"""
Prostate_ULTRASOUND = """
    # Prostate_ULTRASOUND_Report_Extraction_Config.yaml

report_information:
  report_id: "string"            # 报告唯一标识
  patient_id: "string"           # 患者唯一标识
  exam_date: "YYYY-MM-DD"        # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"        # 检查部位，如“前列腺B超”
  conclusion: "string"           # 结论
  CDFI: "string"                 # CDFI相关信息（如适用）

patient_basic_information:
  name: "string"                 # 姓名
  gender: "string"               # 性别
  age: "integer"                 # 年龄
  birth_date: "YYYY-MM-DD"       # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"             # 身高，单位：厘米
  weight_kg: "float"             # 体重，单位：公斤
  medical_record_number: "string" # 病历号
  contact_information: "string"  # 联系方式
  allergy_history: "string"      # 过敏史
  family_history: "string"       # 家族病史
  past_medical_history: "string" # 既往病史
  smoking_history: "string"      # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

organ_extraction:
  prostate:
    volume_ml: "float"                   # 前列腺容积，单位：毫升
    length_cm: "float"                   # 前列腺长度，单位：厘米
    width_cm: "float"                    # 前列腺宽度，单位：厘米
    height_cm: "float"                   # 前列腺高度，单位：厘米
    shape: "string"                      # 前列腺形态，如“对称”、“不对称”
    echotexture: "string"                # 前列腺回声特性，如“均匀回声”、“不均匀回声”
    margins: "string"                    # 前列腺边界描述，如“清晰”、“模糊”
    presence_of_calculus: "boolean"       # 是否存在钙化
    calculus_count: "integer"            # 钙化数量
    calculus_location: "string"          # 钙化位置，如“中央区”、“周边区”
    presence_of_mass: "boolean"          # 是否存在肿块
    mass_size_cm: "float"                # 肿块大小，单位：厘米
    mass_characteristics: "string"       # 肿块特征，如“边界清晰”、“边界不规则”
    presence_of_adenoma: "boolean"       # 是否存在腺瘤
    adenoma_size_cm: "float"             # 腺瘤大小，单位：厘米
    prostatic_hypertrophy: "boolean"     # 是否存在前列腺肥大
    post_void_residual_volume_ml: "float" # 尿后残余量，单位：毫升
    prostatic_caliber_mm: "float"         # 前列腺口径，单位：毫米

prostate_lesions:
  masses:
    - lesion_id: "string"               # 肿块唯一标识
      location: "string"                # 肿块具体位置，如“左叶”、“右叶”
      size_cm: "float"                  # 肿块大小，单位：厘米
      shape: "string"                   # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      boundary: "string"                # 边界描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"            # 回声特性，如“低回声”、“等回声”、“高回声”
      posterior_features: "string"     # 后方特征，如“后方声影”、“后方声像增强”、“无后方改变”
      vascularity: "string"            # 血流情况，如“血流丰富”、“血流少”、“无血流”
      suspected_diagnosis: "string"    # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"    # 其他特征描述，如“钙化”、“囊性变”等

quantitative_metrics:
  prostate_volume_ml: "float"                  # 前列腺体积，单位：毫升
  post_void_residual_volume_ml: "float"        # 尿后残余量，单位：毫升
  prostatic_wall_thickness_mm: "float"         # 前列腺壁厚度，单位：毫米
  prostatic_caliber_statistics_mm: "string"    # 前列腺口径统计，如“平均口径20mm，最大口径25mm”

diagnostic_opinion:
  accurate_diagnosis: "string"                  # 准确的诊断名称

comparative_study:
  compared_with_past_ultrasound: "string"       # 与既往超声影像对比描述
  change_description: "string"                  # 变化描述，如“增大”、“缩小”等

report_details:
  report_generated_date: "YYYY-MM-DD"           # 报告生成日期
  report_generated_time: "HH:MM"                # 报告生成时间
  radiologist_name: "string"                    # 放射科医生姓名
  radiologist_signature: "string"               # 放射科医生签名
  report_number: "string"                       # 报告编号
  remarks: "string"                             # 备注

attachments_and_additional_info:
  image_links:                                  # 影像图像链接列表
    - "string"                                  # 例如："http://example.com/image1"
    - "string"                                  # 例如："http://example.com/image2"
  contrast_enhanced_images:                     # 对比增强图像链接列表（如适用）
    - "string"                                  # 例如："http://example.com/ce_image1"
    - "string"                                  # 例如："http://example.com/ce_image2"
  MPR_images:                                   # 多平面重建图像链接列表（如适用）
    - "string"                                  # 例如："http://example.com/mpr_image1"
    - "string"                                  # 例如："http://example.com/mpr_image2"
  reconstructed_3D_images:                      # 三维重建图像链接列表（如适用）
    - "string"                                  # 例如："http://example.com/3d_image1"
    - "string"                                  # 例如："http://example.com/3d_image2"
  external_reports:                             # 外部相关报告链接列表（如适用）
    - "string"                                  # 例如："http://example.com/external_report1"
    - "string"                                  # 例如："http://example.com/external_report2"
  additional_documents:                         # 其他补充文件链接列表（如适用）
    - "string"                                  # 例如："http://example.com/doc1"
    - "string"                                  # 例如："http://example.com/doc2"
  report_notes:                                 # 报告附注（如适用）
    - "string"                                  # 例如："建议进行前列腺特异性抗原（PSA）检测"
    - "string"                                  # 例如："推荐进行穿刺活检"

"""
Pulmonary_CT = """
    # Pulmonary_CT_Report_Extraction_Config.yaml

report_information:
  report_id: "string"            # 报告唯一标识
  patient_id: "string"           # 患者唯一标识
  exam_date: "YYYY-MM-DD"        # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"        # 检查部位，如“肺部”
  conclusion: "string"           # 结论
  CDFI: "string"                 # CDFI相关信息

# patient_basic_information:
#   name: "string"                 # 姓名
#   gender: "string"               # 性别
#   age: "integer"                 # 年龄
#   birth_date: "YYYY-MM-DD"       # 出生日期，格式：YYYY-MM-DD
#   height_cm: "float"             # 身高，单位：厘米
#   weight_kg: "float"             # 体重，单位：公斤
#   medical_record_number: "string" # 病历号
#   contact_information: "string"  # 联系方式
#   allergy_history: "string"      # 过敏史
#   family_history: "string"       # 家族病史
#   past_medical_history: "string" # 既往病史
#   smoking_history: "string"      # 吸烟史
#   occupational_exposure_history: "string" # 职业暴露史

organ_extraction:
  Organ_aorta: "string"                  # 主动脉描述
  Organ_aortic_arch: "string"            # 主动脉弓描述
  Organ_cardiac_shadow: "string"         # 心影描述
  Organ_trachea: "string"                # 气管描述
  Organ_mediastinum: "string"            # 纵膈描述
  Organ_costophrenic_angle: "string"     # 肋膈角描述
  Organ_pulmonary_texture: "string"      # 肺纹理描述
  Organ_pulmonary_field: "string"        # 肺野描述
  Organ_hilar_region: "string"           # 肺门描述
  Organ_thoracic_cage: "string"          # 胸廓描述
  Organ_pleura: "string"                 # 胸膜描述
  Organ_diaphragm_surface: "string"       # 膈面描述
  Organ_skeleton: "string"               # 骨骼描述

space_occupying_lesions:
  - lesion_id: "string"                   # 占位病变唯一标识
    lesion_type: "string"                 # 占位病变类型，如“肺肿瘤”
    lesion_subtype: "string"              # 占位病变子类型，如“恶性”
    location: "string"                    # 占位病变位置，如“左肺上叶”
    size_long_axis_cm: "float"            # 长轴尺寸，单位：厘米
    size_short_axis_cm: "float"           # 短轴尺寸，单位：厘米，若无则为null
    density: "string"                     # 密度描述，如“实性”
    shape: "string"                       # 形态描述，如“不规则”
    edge: "string"                        # 边缘描述，如“边缘模糊”
    number: "string"                      # 数目，如“单发”
    suspected_diagnosis: "string"         # 疑似诊断，如“肺癌”
    surrounding_tissue: "string"          # 周围组织结构描述，如“周围有纤维化”
    contrast_enhancement: "string"        # 对比增强情况，如“增强明显”
    additional_features: "string"         # 其他特征描述，如“无”

quantitative_metrics:
  lung_volume_L: "float"                     # 肺容量，单位：升
  lung_density_distribution: "string"        # 肺密度分布描述
  nodules_statistics: "string"               # 结节数量和大小统计
  blood_vessels_distribution: "string"       # 血管分布和直径描述

diagnostic_opinion:
  accurate_diagnosis: "string"               # 准确的诊断名称

comparative_study:
  compared_with_past_CT: "string"            # 与既往CT影像对比描述
  change_description: "string"               # 变化描述，如“增大”

report_details:
  report_generated_date: "YYYY-MM-DD"        # 报告生成日期
  report_generated_time: "HH:MM"             # 报告生成时间
  radiologist_name: "string"                 # 放射科医生姓名
  radiologist_signature: "string"            # 放射科医生签名
  report_number: "string"                    # 报告编号
  remarks: "string"                          # 备注

attachments_and_additional_info:
  image_links:                               # 影像图像链接列表
    - "string"
    - "string"
  contrast_enhanced_images:                  # 对比增强图像链接列表
    - "string"
    - "string"
  MPR_images:                                # 多平面重建图像链接列表
    - "string"
    - "string"
  reconstructed_3D_images:                   # 三维重建图像链接列表
    - "string"
    - "string"

"""
Pulmonary_Function_Test = """
    # Pulmonary_Function_Test_Report_Extraction_Config.yaml

report_information:
  report_id: "string"                  # 报告唯一标识
  patient_id: "string"                 # 患者唯一标识
  exam_date: "YYYY-MM-DD"              # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"              # 检查部位，如“肺功能测试”
  conclusion: "string"                 # 结论
  recommendations: "string"            # 建议（如适用）

patient_basic_information:
  name: "string"                       # 姓名
  gender: "string"                     # 性别
  age: "integer"                       # 年龄
  birth_date: "YYYY-MM-DD"             # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"                   # 身高，单位：厘米
  weight_kg: "float"                   # 体重，单位：公斤
  medical_record_number: "string"      # 病历号
  contact_information: "string"        # 联系方式
  allergy_history: "string"            # 过敏史
  family_history: "string"             # 家族病史
  past_medical_history: "string"       # 既往病史
  smoking_history: "string"            # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

test_parameters:
  device_type: "string"                 # 使用设备类型，如“Spirolab III”
  technician_name: "string"             # 操作技师姓名
  pre_test_instructions: "string"       # 术前指导
  test_conditions: "string"             # 测试条件，如“静息状态下进行”

spirometry_results:
  FEV1:
    value_l: "float"                     # FEV1值，单位：升
    percentage_predicted: "float"        # 相对于预测值的百分比，单位：%
    interpretation: "string"             # 解释，如“正常”、“限制性通气障碍”等

  FVC:
    value_l: "float"                     # FVC值，单位：升
    percentage_predicted: "float"        # 相对于预测值的百分比，单位：%
    interpretation: "string"             # 解释，如“正常”、“限制性通气障碍”等

  FEV1_FVC_ratio:
    value_percentage: "float"            # FEV1/FVC比值，单位：%
    interpretation: "string"             # 解释，如“正常”、“阻塞性通气障碍”等

  PEFR:
    value_l_min: "float"                 # 峰值呼气流速，单位：升/分钟
    percentage_predicted: "float"        # 相对于预测值的百分比，单位：%
    interpretation: "string"             # 解释，如“正常”、“受限”等

  FEF25_75:
    value_l_sec: "float"                 # 25-75%用力呼气流速，单位：升/秒
    percentage_predicted: "float"        # 相对于预测值的百分比，单位：%
    interpretation: "string"             # 解释，如“正常”、“受限”等

lung_volumes:
  TLC:
    value_l: "float"                     # 总肺容量，单位：升
    percentage_predicted: "float"        # 相对于预测值的百分比，单位：%
    interpretation: "string"             # 解释，如“正常”、“增加”、“减少”等

  RV:
    value_l: "float"                     # 残余容量，单位：升
    percentage_predicted: "float"        # 相对于预测值的百分比，单位：%
    interpretation: "string"             # 解释，如“正常”、“增加”、“减少”等

  RV_TLC_ratio:
    value_percentage: "float"            # RV/TLC比值，单位：%
    interpretation: "string"             # 解释，如“正常”、“气道阻塞”等

diffusion_capacity:
  DLCO:
    value_ml_min_mmHg: "float"           # 一氧化碳弥散能力，单位：ml/min/mmHg
    percentage_predicted: "float"        # 相对于预测值的百分比，单位：%
    interpretation: "string"             # 解释，如“正常”、“减少”等

  DLCO_alveolar_volume_ratio:
    value_percentage: "float"            # DLCO/VA比值，单位：%
    interpretation: "string"             # 解释，如“正常”、“肺间质病变”等

respiratory_mechanics:
  airway_resistance:
    value_cmH2O_s_L: "float"             # 气道阻力，单位：cmH2O·s/L
    interpretation: "string"             # 解释，如“正常”、“增加”、“减少”等

  lung_compliance:
    value_ml_cmH2O: "float"              # 肺顺应性，单位：ml/cmH2O
    interpretation: "string"             # 解释，如“正常”、“减少”、“增加”等

quantitative_metrics:
  spirometry_percent_predicted:
    FEV1: "float"                         # FEV1相对于预测值的百分比
    FVC: "float"                          # FVC相对于预测值的百分比
    FEV1_FVC_ratio: "float"               # FEV1/FVC比值相对于预测值的百分比

  lung_volumes_percent_predicted:
    TLC: "float"                          # TLC相对于预测值的百分比
    RV: "float"                           # RV相对于预测值的百分比

  diffusion_capacity_percent_predicted:
    DLCO: "float"                         # DLCO相对于预测值的百分比
    DLCO_alveolar_volume_ratio: "float"    # DLCO/VA比值相对于预测值的百分比

diagnostic_opinion:
  accurate_diagnosis: "string"            # 准确的诊断名称

comparative_study:
  compared_with_past_pft: "string"        # 与既往肺功能测试对比描述
  change_description: "string"            # 变化描述，如“FEV1下降”、“TLC增加”等

report_details:
  report_generated_date: "YYYY-MM-DD"     # 报告生成日期
  report_generated_time: "HH:MM"          # 报告生成时间
  pulmonologist_name: "string"            # 肺科医生姓名
  pulmonologist_signature: "string"       # 肺科医生签名
  report_number: "string"                 # 报告编号
  remarks: "string"                       # 备注

attachments_and_additional_info:
  image_links:                            # 影像图像链接列表
    - "string"                            # 例如："http://example.com/pft_image1"
    - "string"                            # 例如："http://example.com/pft_image2"
  external_reports:                       # 外部相关报告链接列表（如适用）
    - "string"                            # 例如："http://example.com/external_report1"
    - "string"                            # 例如："http://example.com/external_report2"
  additional_documents:                   # 其他补充文件链接列表（如适用）
    - "string"                            # 例如："http://example.com/doc1"
    - "string"                            # 例如："http://example.com/doc2"
  report_notes:                           # 报告附注（如适用）
    - "string"                            # 例如："建议进行高分辨率CT扫描"
    - "string"                            # 例如："推荐进行血气分析"

"""
Resting_ECG = """
    # Resting_ECG_Report_Extraction_Config.yaml

report_information:
  report_id: "string"                  # 报告唯一标识
  patient_id: "string"                 # 患者唯一标识
  exam_date: "YYYY-MM-DD"              # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"              # 检查部位，如“静息心电图”
  conclusion: "string"                 # 结论
  recommendations: "string"            # 建议（如适用）
  
patient_basic_information:
  name: "string"                       # 姓名
  gender: "string"                     # 性别
  age: "integer"                       # 年龄
  birth_date: "YYYY-MM-DD"             # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"                   # 身高，单位：厘米
  weight_kg: "float"                   # 体重，单位：公斤
  medical_record_number: "string"      # 病历号
  contact_information: "string"        # 联系方式
  allergy_history: "string"            # 过敏史
  family_history: "string"             # 家族病史
  past_medical_history: "string"       # 既往病史
  smoking_history: "string"            # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

ECG_findings:
  heart_rate_bpm: "integer"            # 心率，单位：次/分钟
  rhythm: "string"                      # 心律，如“窦性心律”、“房颤”等
  pr_interval_ms: "float"               # PR间期，单位：毫秒
  qrs_duration_ms: "float"              # QRS波宽度，单位：毫秒
  qt_interval_ms: "float"               # QT间期，单位：毫秒
  qt_corrected: "float"                 # 校正QT间期（QTc），单位：毫秒
  axis_degrees: "integer"                # 电轴，单位：度
  p_wave: "string"                       # P波特征，如“正常”、“倒置”等
  q_wave: "string"                       # Q波特征，如“正常”、“异常”等
  r_wave: "string"                       # R波特征，如“正常”、“增高”等
  s_wave: "string"                       # S波特征，如“正常”、“增深”等
  st_segment: "string"                   # ST段特征，如“抬高”、“压低”、“正常”等
  t_wave: "string"                       # T波特征，如“倒置”、“高尖”、“低平”等
  abnormal_findings: "string"            # 异常发现，如“心肌缺血”、“心肌梗死”、“室性早搏”等

quantitative_metrics:
  pr_interval_mean_ms: "float"           # PR间期平均值，单位：毫秒
  qrs_duration_mean_ms: "float"          # QRS波宽度平均值，单位：毫秒
  qt_interval_mean_ms: "float"           # QT间期平均值，单位：毫秒
  qt_corrected_mean_ms: "float"          # 校正QT间期平均值，单位：毫秒
  heart_rate_statistics_bpm: "string"    # 心率统计，如“平均心率70次/分钟，范围60-80次/分钟”

diagnostic_opinion:
  accurate_diagnosis: "string"            # 准确的诊断名称

comparative_study:
  compared_with_past_ecg: "string"        # 与既往心电图对比描述
  change_description: "string"            # 变化描述，如“心律由窦性转为房颤”、“QTc延长”等

report_details:
  report_generated_date: "YYYY-MM-DD"     # 报告生成日期
  report_generated_time: "HH:MM"          # 报告生成时间
  cardiologist_name: "string"             # 心脏病专科医生姓名
  cardiologist_signature: "string"        # 心脏病专科医生签名
  report_number: "string"                 # 报告编号
  remarks: "string"                       # 备注

attachments_and_additional_info:
  image_links:                            # 影像图像链接列表
    - "string"                            # 例如："http://example.com/ecg_image1"
    - "string"                            # 例如："http://example.com/ecg_image2"
  external_reports:                       # 外部相关报告链接列表（如适用）
    - "string"                            # 例如："http://example.com/external_report1"
    - "string"                            # 例如："http://example.com/external_report2"
  additional_documents:                   # 其他补充文件链接列表（如适用）
    - "string"                            # 例如："http://example.com/doc1"
    - "string"                            # 例如："http://example.com/doc2"
  report_notes:                           # 报告附注（如适用）
    - "string"                            # 例如："建议进行动态心电图检查"
    - "string"                            # 例如："推荐进行心脏超声检查"

"""
Spleen_Abdominal_BUS = """
    # Spleen_Abdominal_BUS_Report_Extraction_Config.yaml

report_information:
  report_id: "string"            # 报告唯一标识
  patient_id: "string"           # 患者唯一标识
  exam_date: "YYYY-MM-DD"        # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"        # 检查部位，如“腹部B超”
  conclusion: "string"           # 结论
  CDFI: "string"                 # CDFI相关信息（如适用）

patient_basic_information:
  name: "string"                 # 姓名
  gender: "string"               # 性别
  age: "integer"                 # 年龄
  birth_date: "YYYY-MM-DD"       # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"             # 身高，单位：厘米
  weight_kg: "float"             # 体重，单位：公斤
  medical_record_number: "string" # 病历号
  contact_information: "string"  # 联系方式
  allergy_history: "string"      # 过敏史
  family_history: "string"       # 家族病史
  past_medical_history: "string" # 既往病史
  smoking_history: "string"      # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

organ_extraction:
  spleen:
    size_length_cm: "float"          # 脾脏长度，单位：厘米
    size_width_cm: "float"           # 脾脏宽度，单位：厘米
    size_thickness_cm: "float"       # 脾脏厚度，单位：厘米
    echotexture: "string"            # 脾脏回声特性，如“均匀回声”、“杂乱回声”等
    borders: "string"                # 脾脏边界描述，如“清晰”、“模糊”等
    hilum_visibility: "string"        # 脾门可见性，如“可见”、“不可见”
    vascular_structures: "string"     # 血管结构描述，如“脾动脉形态正常”
    surrounding_tissues: "string"     # 周围组织描述，如“未见肿块”等
    adjacent_organs: "string"         # 邻近器官描述，如“肝脏形态正常”

spleen_lesions:
  masses:
    - lesion_id: "string"             # 肿块唯一标识
      location: "string"              # 肿块具体位置，如“脾上叶”
      size_cm: "float"                # 肿块大小，单位：厘米
      shape: "string"                 # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      margins: "string"               # 边缘描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"           # 回声特性，如“低回声”、“等回声”、“高回声”
      posterior_features: "string"    # 后方特征，如“后方声影”、“后方声像增强”、“无后方改变”
      vascularity: "string"           # 血流情况，如“血流丰富”、“血流少”、“无血流”
      suspected_diagnosis: "string"   # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"   # 其他特征描述，如“钙化”、“囊性变”等

  cysts:
    - cyst_id: "string"               # 囊肿唯一标识
      location: "string"              # 囊肿具体位置，如“脾中叶”
      size_cm: "float"                # 囊肿大小，单位：厘米
      shape: "string"                 # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      margins: "string"               # 边缘描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"           # 回声特性，如“无回声”、“低回声”、“混合回声”
      posterior_features: "string"    # 后方特征，如“无后方改变”、“后方声影”
      vascularity: "string"           # 血流情况，如“无血流”
      suspected_diagnosis: "string"   # 疑似诊断，如“单纯性囊肿”、“复杂囊肿”
      additional_features: "string"   # 其他特征描述，如“囊壁增厚”、“分隔”等

  other_lesions:
    - lesion_id: "string"             # 其他病变唯一标识
      type: "string"                  # 病变类型，如“脾血管瘤”、“脾脏炎症”等
      location: "string"              # 病变具体位置，如“脾下叶”
      size_cm: "float"                # 病变大小，单位：厘米
      shape: "string"                 # 形态描述，如“不规则形”、“结节状”等
      margins: "string"               # 边缘描述，如“模糊”、“分叶”等
      echogenicity: "string"           # 回声特性，如“高回声”、“等回声”等
      posterior_features: "string"    # 后方特征，如“后方声影”、“后方声像增强”
      vascularity: "string"           # 血流情况，如“少”、“无血流”
      suspected_diagnosis: "string"   # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"   # 其他特征描述，如“钙化”、“空洞形成”等

lymph_nodes:
  - node_id: "string"                  # 淋巴结唯一标识
    size_cm: "float"                    # 淋巴结大小，单位：厘米
    location: "string"                  # 位置，如“脾周围”、“腹主动脉旁”等
    morphology: "string"                # 形态描述，如“圆形”、“卵圆形”、“结节状”等
    hilum_visibility: "string"          # 门静脉可见性，如“可见”、“不可见”
    suspicious_features: "string"       # 可疑特征，如“形态不规则”、“边缘模糊”等
    suspected_diagnosis: "string"       # 疑似诊断，如“转移性淋巴结”等

quantitative_metrics:
  spleen_volume_ml: "float"              # 脾脏体积，单位：毫升
  nodules_volume_statistics: "string"     # 结节体积统计
  blood_vessels_distribution: "string"    # 血管分布和直径描述

diagnostic_opinion:
  accurate_diagnosis: "string"            # 准确的诊断名称

comparative_study:
  compared_with_past_ultrasound: "string" # 与既往超声影像对比描述
  change_description: "string"            # 变化描述，如“增大”、“缩小”等

report_details:
  report_generated_date: "YYYY-MM-DD"     # 报告生成日期
  report_generated_time: "HH:MM"          # 报告生成时间
  radiologist_name: "string"              # 放射科医生姓名
  radiologist_signature: "string"         # 放射科医生签名
  report_number: "string"                 # 报告编号
  remarks: "string"                       # 备注

attachments_and_additional_info:
  image_links:                            # 影像图像链接列表
    - "string"
    - "string"
  contrast_enhanced_images:               # 对比增强图像链接列表（如适用）
    - "string"
    - "string"
  MPR_images:                             # 多平面重建图像链接列表（如适用）
    - "string"
    - "string"
  reconstructed_3D_images:                # 三维重建图像链接列表（如适用）
    - "string"
    - "string"

"""
Thyroid_Ultrasound = """
    # Thyroid_Ultrasound_Report_Extraction_Config.yaml

report_information:
  report_id: "string"            # 报告唯一标识
  patient_id: "string"           # 患者唯一标识
  exam_date: "YYYY-MM-DD"        # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"        # 检查部位，如“甲状腺”
  conclusion: "string"           # 结论
  ultrasound_mode: "string"      # 超声模式相关信息，如“彩色多普勒”

patient_basic_information:
  name: "string"                 # 姓名
  gender: "string"               # 性别
  age: "integer"                 # 年龄
  birth_date: "YYYY-MM-DD"       # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"             # 身高，单位：厘米
  weight_kg: "float"             # 体重，单位：公斤
  medical_record_number: "string" # 病历号
  contact_information: "string"  # 联系方式
  allergy_history: "string"      # 过敏史
  family_history: "string"       # 家族病史
  past_medical_history: "string" # 既往病史
  smoking_history: "string"      # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

organ_extraction:
  Organ_thyroid:
    description: "string"              # 甲状腺整体描述
    is_normal: "boolean"               # 甲状腺形态是否正常
    size_cm: "float"                   # 甲状腺大小，单位：厘米
    echotexture: "string"              # 回声特征，如“均匀”
    echogenicity: "string"              # 回声强度，如“等回声”
    margins: "string"                   # 边界描述，如“清晰”
    echogenic_foci: "string"            # 回声灶，如“微钙化”
    calcifications: "string"            # 钙化情况，如“未见明显强回声”
    echo_condition: "string"           # 回声情况，如“未见异常”或“囊实性回声”
    shape: "string"                     # 形状，如“椭圆形”
    morphology: "string"                # 形态，如“形态正常”
    size_status: "string"               # 大小状态，如“大小正常”
    blood_flow: "string"                # 血流情况，如“未见异常血流信号”
    enhancement: "string"               # 强化情况，如“无强化”
    posterior_echo: "string"            # 后方回声，如“无异常”
    elasticity: "string"                # 质地弹性，如“未描述”
    capsule: "string"                   # 包膜情况，如“包膜完整”
    surgical_history: "string"          # 手术情况，如“未描述”

  Organ_larynx: "string"                 # 喉部描述
  Organ_trachea: "string"                # 气管描述
  Organ_cervical_lymph_nodes: "string"   # 颈部淋巴结描述

space_occupying_lesions:
  - lesion_id: "string"                   # 占位病变唯一标识
    lesion_type: "string"                 # 占位病变类型，如“结节”
    lesion_subtype: "string"              # 占位病变子类型，如“实性”
    location: "string"                    # 占位病变位置，如“左叶上极”
    size_long_axis_cm: "float"            # 长轴尺寸，单位：厘米
    size_short_axis_cm: "float"           # 短轴尺寸，单位：厘米，若无则为null
    composition: "string"                 # 组成，如“实性”或“囊实性”
    echogenicity: "string"                 # 回声特性，如“低回声”
    margins: "string"                      # 边缘描述，如“模糊”或“边界光整”
    calcifications: "string"               # 钙化情况，如“微钙化”
    vascularity: "string"                  # 血流情况，如“无”或“丰富”
    shape: "string"                        # 形状，如“边缘不规则”或“类圆形”
    morphology: "string"                   # 形态，如“形态规则”
    aspect_ratio: "string"                 # 纵横比，如“≤”
    number: "integer"                      # 数目，如“多个”
    suspected_diagnosis: "string"          # 疑似诊断，如“良性结节”
    surrounding_tissue: "string"           # 周围组织描述，如“周围无异常”
    additional_features: "string"          # 其他特征描述，如“无囊性变”

quantitative_metrics:
  thyroid_volume_ml: "float"               # 甲状腺体积，单位：毫升
  nodule_count: "integer"                  # 结节数量
  largest_nodule_size_cm: "float"          # 最大结节尺寸，单位：厘米
  vascular_index: "float"                  # 血管指数

lymph_nodes:
  lymph_node_condition: "string"            # 淋巴情况淋巴结情况，如“多发淋巴结”
  activity: "string"                        # 活动度，如“未描述”
  cortex_medulla: "string"                  # 皮髓质，如“皮髓质分界清晰”
  gate: "string"                            # 淋巴门，如“淋巴门结构可见”

diagnostic_opinion:
  accurate_diagnosis: "string"              # 准确的诊断名称

comparative_study:
  compared_with_past_ultrasound: "string"   # 与既往超声影像对比描述
  change_description: "string"             # 变化描述，如“结节增大”

report_details:
  report_generated_date: "YYYY-MM-DD"        # 报告生成日期
  report_generated_time: "HH:MM"             # 报告生成时间
  ultrasonographer_name: "string"            # 超声医师姓名
  ultrasonographer_signature: "string"       # 超声医师签名
  report_number: "string"                    # 报告编号
  remarks: "string"                          # 备注

attachments_and_additional_info:
  image_links:                               # 影像图像链接列表
    - "string"
    - "string"
  cine_loop_videos:                          # 动态影像视频链接列表
    - "string"
    - "string"
  annotated_images:                          # 标注图像链接列表
    - "string"
    - "string"
  3D_reconstructed_images:                   # 三维重建图像链接列表
    - "string"
    - "string"

"""
Ureter_Urinary_Sys_ULTRASOUND = """
    # Ureter_Urinary_Sys_ULTRASOUND_Report_Extraction_Config.yaml

report_information:
  report_id: "string"            # 报告唯一标识
  patient_id: "string"           # 患者唯一标识
  exam_date: "YYYY-MM-DD"        # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"        # 检查部位，如“泌尿系统超声”
  conclusion: "string"           # 结论
  CDFI: "string"                 # CDFI相关信息（如适用）

patient_basic_information:
  name: "string"                 # 姓名
  gender: "string"               # 性别
  age: "integer"                 # 年龄
  birth_date: "YYYY-MM-DD"       # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"             # 身高，单位：厘米
  weight_kg: "float"             # 体重，单位：公斤
  medical_record_number: "string" # 病历号
  contact_information: "string"  # 联系方式
  allergy_history: "string"      # 过敏史
  family_history: "string"       # 家族病史
  past_medical_history: "string" # 既往病史
  smoking_history: "string"      # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

organ_extraction:
  bladder:
    volume_ml: "float"                   # 膀胱容积，单位：毫升
    wall_thickness_mm: "float"           # 膀胱壁厚度，单位：毫米
    echotexture: "string"                # 膀胱回声特性，如“均匀回声”、“不均匀回声”
    presence_of_diverticula: "boolean"    # 是否存在憩室
    diverticula_count: "integer"         # 憩室数量
    diverticula_size_cm: "float"         # 憩室大小，单位：厘米
    presence_of_calculus: "boolean"       # 是否存在结石
    calculus_count: "integer"            # 结石数量
    calculus_size_cm: "float"            # 结石大小，单位：厘米
    presence_of_mass: "boolean"          # 是否存在肿块
    mass_size_cm: "float"                # 肿块大小，单位：厘米
    mass_characteristics: "string"       # 肿块特征，如“边界清晰”、“边界模糊”
    post_void_residual_volume_ml: "float" # 尿后残余量，单位：毫升
    bladder_shape: "string"               # 膀胱形态，如“规则”、“不规则”
    bladder_position: "string"            # 膀胱位置，如“位于下腹部正中”

  ureters:
    - side: "string"                      # 侧别，如“左侧”、“右侧”
      diameter_mm: "float"                # 输尿管直径，单位：毫米
      length_cm: "float"                   # 输尿管长度，单位：厘米
      wall_thickness_mm: "float"           # 输尿管壁厚度，单位：毫米
      echotexture: "string"                # 输尿管回声特性，如“均匀回声”、“不均匀回声”
      presence_of_calculus: "boolean"       # 是否存在结石
      calculus_size_mm: "float"            # 结石大小，单位：毫米
      calculus_location: "string"          # 结石位置，如“近端”、“中段”、“远端”
      presence_of_stricture: "boolean"      # 是否存在狭窄
      stricture_length_cm: "float"         # 狭窄长度，单位：厘米
      hydronephrosis_grade: "integer"       # 肾盂积水分级，如1-4级
      bladder_ureteral_junction: "string"   # 膀胱-输尿管交界处描述，如“正常”、“扩张”

bladder_lesions:
  masses:
    - lesion_id: "string"               # 肿块唯一标识
      location: "string"                # 肿块具体位置，如“膀胱底部”
      size_cm: "float"                  # 肿块大小，单位：厘米
      shape: "string"                   # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      boundary: "string"                # 边界描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"            # 回声特性，如“低回声”、“等回声”、“高回声”
      posterior_features: "string"     # 后方特征，如“后方声影”、“后方声像增强”、“无后方改变”
      vascularity: "string"            # 血流情况，如“血流丰富”、“血流少”、“无血流”
      suspected_diagnosis: "string"    # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"    # 其他特征描述，如“钙化”、“囊性变”等

quantitative_metrics:
  bladder_volume_ml: "float"                  # 膀胱体积，单位：毫升
  post_void_residual_volume_ml: "float"       # 尿后残余量，单位：毫升
  bladder_wall_thickness_statistics_mm: "string" # 膀胱壁厚度统计，如“平均厚度2.5mm，最大厚度3.0mm”
  ureter_diameter_statistics_mm: "string"        # 输尿管直径统计，如“左侧平均直径5mm，右侧平均直径6mm”
  hydronephrosis_grade: "integer"               # 肾盂积水分级，如1-4级

diagnostic_opinion:
  accurate_diagnosis: "string"                # 准确的诊断名称

comparative_study:
  compared_with_past_ultrasound: "string"     # 与既往超声影像对比描述
  change_description: "string"                # 变化描述，如“增大”、“缩小”等

report_details:
  report_generated_date: "YYYY-MM-DD"         # 报告生成日期
  report_generated_time: "HH:MM"              # 报告生成时间
  radiologist_name: "string"                  # 放射科医生姓名
  radiologist_signature: "string"             # 放射科医生签名
  report_number: "string"                     # 报告编号
  remarks: "string"                           # 备注

attachments_and_additional_info:
  image_links:                                # 影像图像链接列表
    - "string"                                # 例如："http://example.com/image1"
    - "string"                                # 例如："http://example.com/image2"
  contrast_enhanced_images:                   # 对比增强图像链接列表（如适用）
    - "string"                                # 例如："http://example.com/ce_image1"
    - "string"                                # 例如："http://example.com/ce_image2"
  MPR_images:                                 # 多平面重建图像链接列表（如适用）
    - "string"                                # 例如："http://example.com/mpr_image1"
    - "string"                                # 例如："http://example.com/mpr_image2"
  reconstructed_3D_images:                    # 三维重建图像链接列表（如适用）
    - "string"                                # 例如："http://example.com/3d_image1"
    - "string"                                # 例如："http://example.com/3d_image2"
  external_reports:                           # 外部相关报告链接列表（如适用）
    - "string"                                # 例如："http://example.com/external_report1"
    - "string"                                # 例如："http://example.com/external_report2"
  additional_documents:                       # 其他补充文件链接列表（如适用）
    - "string"                                # 例如："http://example.com/doc1"
    - "string"                                # 例如："http://example.com/doc2"
  report_notes:                               # 报告附注（如适用）
    - "string"                                # 例如："建议进行进一步的超声检查"
    - "string"                                # 例如："推荐进行MRI扫描"

"""
Uterus_Abdominal_BUS = """
    # Uterus_Abdominal_BUS_Report_Extraction_Config.yaml

report_information:
  report_id: "string"            # 报告唯一标识
  patient_id: "string"           # 患者唯一标识
  exam_date: "YYYY-MM-DD"        # 检查日期，格式：YYYY-MM-DD
  exam_location: "string"        # 检查部位，如“腹部B超”
  conclusion: "string"           # 结论
  CDFI: "string"                 # CDFI相关信息（如适用）

patient_basic_information:
  name: "string"                 # 姓名
  gender: "string"               # 性别
  age: "integer"                 # 年龄
  birth_date: "YYYY-MM-DD"       # 出生日期，格式：YYYY-MM-DD
  height_cm: "float"             # 身高，单位：厘米
  weight_kg: "float"             # 体重，单位：公斤
  medical_record_number: "string" # 病历号
  contact_information: "string"  # 联系方式
  allergy_history: "string"      # 过敏史
  family_history: "string"       # 家族病史
  past_medical_history: "string" # 既往病史
  smoking_history: "string"      # 吸烟史
  occupational_exposure_history: "string" # 职业暴露史

organ_extraction:
  uterus:
    position: "string"                  # 子宫位置，如“位于盆腔正中”
    anteversion_angle_deg: "float"       # 前倾角度，单位：度
    anteflexion_angle_deg: "float"       # 前屈角度，单位：度
    size_length_cm: "float"              # 子宫长度，单位：厘米
    size_width_cm: "float"               # 子宫宽度，单位：厘米
    size_thickness_cm: "float"           # 子宫厚度，单位：厘米
    echotexture: "string"                # 子宫回声特性，如“均匀回声”、“杂乱回声”等
    myometrium_echogenicity: "string"    # 子宫肌层回声特性，如“正常”、“高回声”、“低回声”
    endometrium_thickness_cm: "float"    # 子宫内膜厚度，单位：厘米
    endometrium_echogenicity: "string"   # 子宫内膜回声特性，如“均匀回声”、“不均匀回声”
    myometrial_hyperplasia: "boolean"    # 是否存在子宫肌层增生
    fibroids_present: "boolean"          # 是否存在子宫肌瘤
    fibroids_count: "integer"            # 子宫肌瘤数量
    fibroids_size_cm: "float"            # 子宫肌瘤大小，单位：厘米
    polyps_present: "boolean"            # 是否存在子宫息肉
    polyps_count: "integer"              # 子宫息肉数量
    polyps_size_cm: "float"              # 子宫息肉大小，单位：厘米
    adenomyosis_present: "boolean"       # 是否存在子宫腺肌症
    adjacent_organs: "string"            # 邻近器官描述，如“膀胱形态正常”

uterus_lesions:
  fibroids:
    - fibroid_id: "string"               # 肌瘤唯一标识
      location: "string"                  # 肌瘤具体位置，如“子宫体部”
      size_cm: "float"                    # 肌瘤大小，单位：厘米
      shape: "string"                     # 形态描述，如“圆形”、“椭圆形”、“不规则形”
      margins: "string"                   # 边缘描述，如“清晰”、“模糊”、“不规则”
      echogenicity: "string"               # 回声特性，如“低回声”、“等回声”、“高回声”
      posterior_features: "string"        # 后方特征，如“后方声影”、“后方声像增强”、“无后方改变”
      vascularity: "string"               # 血流情况，如“血流丰富”、“血流少”、“无血流”
      suspected_diagnosis: "string"       # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"       # 其他特征描述，如“钙化”、“囊性变”等

  polyps:
    - polyp_id: "string"                  # 息肉唯一标识
      location: "string"                   # 息肉具体位置，如“子宫内膜”
      size_cm: "float"                     # 息肉大小，单位：厘米
      echogenicity: "string"                # 回声特性，如“低回声”、“等回声”、“高回声”
      margins: "string"                    # 边缘描述，如“光滑”、“不规则”
      suspected_diagnosis: "string"        # 疑似诊断，如“良性息肉”、“恶性息肉”
      additional_features: "string"        # 其他特征描述，如“钙化”、“血流丰富”等

  other_lesions:
    - lesion_id: "string"                  # 其他病变唯一标识
      type: "string"                       # 病变类型，如“子宫内膜息肉”、“子宫内膜异位症”等
      location: "string"                   # 病变具体位置，如“子宫内膜”
      size_cm: "float"                     # 病变大小，单位：厘米
      shape: "string"                      # 形态描述，如“不规则形”、“结节状”等
      margins: "string"                    # 边缘描述，如“模糊”、“分叶”等
      echogenicity: "string"                # 回声特性，如“高回声”、“等回声”等
      posterior_features: "string"         # 后方特征，如“后方声影”、“后方声像增强”
      vascularity: "string"                # 血流情况，如“少”、“无血流”
      suspected_diagnosis: "string"        # 疑似诊断，如“良性”、“恶性”
      additional_features: "string"        # 其他特征描述，如“钙化”、“空洞形成”等

quantitative_metrics:
  uterus_volume_ml: "float"                # 子宫体积，单位：毫升
  fibroids_volume_statistics: "string"      # 肌瘤体积统计，如“子宫体部1个（3.0cm）”
  polyps_volume_statistics: "string"        # 息肉体积统计，如“子宫内膜1个（0.5cm）”
  blood_vessels_distribution: "string"     # 血管分布和直径描述

diagnostic_opinion:
  accurate_diagnosis: "string"             # 准确的诊断名称

comparative_study:
  compared_with_past_ultrasound: "string"  # 与既往超声影像对比描述
  change_description: "string"             # 变化描述，如“增大”、“缩小”等

report_details:
  report_generated_date: "YYYY-MM-DD"      # 报告生成日期
  report_generated_time: "HH:MM"           # 报告生成时间
  radiologist_name: "string"               # 放射科医生姓名
  radiologist_signature: "string"          # 放射科医生签名
  report_number: "string"                  # 报告编号
  remarks: "string"                        # 备注

attachments_and_additional_info:
  image_links:                             # 影像图像链接列表
    - "string"
    - "string"
  contrast_enhanced_images:                # 对比增强图像链接列表（如适用）
    - "string"
    - "string"
  MPR_images:                              # 多平面重建图像链接列表（如适用）
    - "string"
    - "string"
  reconstructed_3D_images:                 # 三维重建图像链接列表（如适用）
    - "string"
    - "string"

"""