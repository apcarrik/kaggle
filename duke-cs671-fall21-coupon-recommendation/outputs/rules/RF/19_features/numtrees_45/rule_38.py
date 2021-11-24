def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[4]>0:
		# {"feature": "Gender", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[16]>0.0:
				# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[13]>1.0:
					# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[11]>17:
						return 'True'
					elif obj[11]<=17:
						return 'False'
					else: return 'False'
				elif obj[13]<=1.0:
					return 'True'
				else: return 'True'
			elif obj[16]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[6]>0:
			return 'True'
		else: return 'True'
	elif obj[4]<=0:
		return 'False'
	else: return 'False'
