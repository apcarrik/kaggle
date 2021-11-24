def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Weather", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[1]<=0:
		# {"feature": "Income", "instances": 42, "metric_value": 0.9403, "depth": 2}
		if obj[10]<=6:
			# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.99, "depth": 3}
			if obj[13]>0.0:
				# {"feature": "Children", "instances": 31, "metric_value": 0.9629, "depth": 4}
				if obj[7]<=0:
					# {"feature": "Direction_same", "instances": 17, "metric_value": 0.6723, "depth": 5}
					if obj[14]<=0:
						# {"feature": "Passanger", "instances": 14, "metric_value": 0.3712, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[15]<=1:
									return 'False'
								elif obj[15]>1:
									return 'True'
								else: return 'True'
							elif obj[2]>3:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[14]>0:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[7]>0:
					# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[9]>4:
						# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]>2:
							return 'True'
						else: return 'True'
					elif obj[9]<=4:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[13]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[10]>6:
			return 'True'
		else: return 'True'
	elif obj[1]>0:
		# {"feature": "Gender", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[5]<=0:
			return 'False'
		elif obj[5]>0:
			# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[9]>6:
				return 'False'
			elif obj[9]<=6:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
