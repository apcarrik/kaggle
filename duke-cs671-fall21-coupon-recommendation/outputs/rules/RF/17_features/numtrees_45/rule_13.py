def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[10]<=11:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Bar", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[12]<=0.0:
				# {"feature": "Age", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[6]>1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[14]<=0.0:
						# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=0:
							return 'False'
						elif obj[4]>0:
							return 'True'
						else: return 'True'
					elif obj[14]>0.0:
						return 'True'
					else: return 'True'
				elif obj[6]<=1:
					return 'False'
				else: return 'False'
			elif obj[12]>0.0:
				return 'False'
			else: return 'False'
		elif obj[3]>2:
			# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[5]<=0:
					return 'True'
				elif obj[5]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[10]>11:
		return 'False'
	else: return 'False'
