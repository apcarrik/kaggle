def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[3]>1:
		# {"feature": "Coupon_validity", "instances": 23, "metric_value": 0.9986, "depth": 2}
		if obj[4]>0:
			# {"feature": "Gender", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[6]<=3:
						return 'False'
					elif obj[6]>3:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[9]<=2:
							return 'True'
						elif obj[9]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[5]>0:
				return 'False'
			else: return 'False'
		elif obj[4]<=0:
			# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[16]<=2:
				return 'True'
			elif obj[16]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[9]<=4:
			return 'False'
		elif obj[9]>4:
			return 'True'
		else: return 'True'
	else: return 'False'
