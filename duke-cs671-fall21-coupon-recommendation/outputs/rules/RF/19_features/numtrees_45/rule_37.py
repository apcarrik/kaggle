def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[7]<=2:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[16]<=1.0:
				return 'True'
			elif obj[16]>1.0:
				return 'False'
			else: return 'False'
		elif obj[4]>3:
			return 'False'
		else: return 'False'
	elif obj[7]>2:
		return 'True'
	else: return 'True'
