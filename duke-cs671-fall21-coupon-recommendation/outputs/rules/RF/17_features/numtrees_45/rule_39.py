def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[6]<=4:
		# {"feature": "Income", "instances": 14, "metric_value": 0.9852, "depth": 2}
		if obj[11]>2:
			# {"feature": "Gender", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[5]>0:
				# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[13]<=0.0:
					return 'True'
				elif obj[13]>0.0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[9]<=2:
						return 'False'
					elif obj[9]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]<=0:
				return 'False'
			else: return 'False'
		elif obj[11]<=2:
			return 'True'
		else: return 'True'
	elif obj[6]>4:
		return 'True'
	else: return 'True'
