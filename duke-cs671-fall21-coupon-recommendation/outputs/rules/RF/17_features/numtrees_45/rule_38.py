def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[16]<=2:
		# {"feature": "Maritalstatus", "instances": 20, "metric_value": 1.0, "depth": 2}
		if obj[7]<=1:
			# {"feature": "Coupon", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[3]>1:
				# {"feature": "Income", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[11]<=4:
					# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[2]>2:
						return 'True'
					elif obj[2]<=2:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[6]<=3:
							return 'False'
						elif obj[6]>3:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[11]>4:
					return 'False'
				else: return 'False'
			elif obj[3]<=1:
				return 'False'
			else: return 'False'
		elif obj[7]>1:
			return 'True'
		else: return 'True'
	elif obj[16]>2:
		return 'False'
	else: return 'False'
