def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Maritalstatus", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[7]>0:
		# {"feature": "Age", "instances": 25, "metric_value": 0.9896, "depth": 2}
		if obj[6]<=5:
			# {"feature": "Time", "instances": 21, "metric_value": 0.9984, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[10]<=13:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[3]>0:
						# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[16]<=2:
							return 'False'
						elif obj[16]>2:
							# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0:
								return 'True'
							elif obj[4]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[10]>13:
					return 'True'
				else: return 'True'
			elif obj[2]>1:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[10]<=7:
					return 'True'
				elif obj[10]>7:
					# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=0:
						return 'False'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[6]>5:
			return 'True'
		else: return 'True'
	elif obj[7]<=0:
		# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[6]>0:
			return 'False'
		elif obj[6]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
