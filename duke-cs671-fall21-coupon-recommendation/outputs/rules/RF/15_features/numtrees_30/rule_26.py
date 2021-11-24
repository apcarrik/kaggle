def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Coupon", "instances": 27, "metric_value": 0.9751, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Passanger", "instances": 19, "metric_value": 0.998, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Age", "instances": 16, "metric_value": 0.9887, "depth": 4}
				if obj[5]>0:
					# {"feature": "Direction_same", "instances": 14, "metric_value": 1.0, "depth": 5}
					if obj[13]<=0:
						# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[10]<=1.0:
							# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[6]>0:
								return 'False'
							elif obj[6]<=0:
								# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[9]<=6:
									return 'True'
								elif obj[9]>6:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[10]>1.0:
							# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[14]>1:
								return 'True'
							elif obj[14]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[13]>0:
						return 'True'
					else: return 'True'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[2]>3:
			# {"feature": "Bar", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[10]<=2.0:
				return 'False'
			elif obj[10]>2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]>3:
		# {"feature": "Children", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[6]<=0:
			return 'True'
		elif obj[6]>0:
			return 'False'
		else: return 'False'
	else: return 'True'
