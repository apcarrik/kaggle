def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Age", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[6]<=3:
		# {"feature": "Restaurant20to50", "instances": 46, "metric_value": 0.9781, "depth": 2}
		if obj[14]>0.0:
			# {"feature": "Income", "instances": 41, "metric_value": 0.9961, "depth": 3}
			if obj[11]<=3:
				# {"feature": "Gender", "instances": 23, "metric_value": 0.8865, "depth": 4}
				if obj[5]>0:
					return 'False'
				elif obj[5]<=0:
					# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[9]<=2:
						# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[12]>0.0:
							return 'True'
						elif obj[12]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[9]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[11]>3:
				# {"feature": "Passanger", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[15]<=0:
						# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[13]<=3.0:
							# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[3]<=3:
								# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[1]<=0:
									return 'True'
								elif obj[1]>0:
									# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4]<=0:
										return 'False'
									elif obj[4]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[3]>3:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]<=1:
									return 'False'
								elif obj[2]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[13]>3.0:
							return 'False'
						else: return 'False'
					elif obj[15]>0:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[14]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[6]>3:
		# {"feature": "Coupon_validity", "instances": 39, "metric_value": 0.8582, "depth": 2}
		if obj[4]<=0:
			# {"feature": "Passanger", "instances": 21, "metric_value": 0.4537, "depth": 3}
			if obj[0]>0:
				# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.2864, "depth": 4}
				if obj[13]<=3.0:
					return 'True'
				elif obj[13]>3.0:
					# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[4]>0:
			# {"feature": "Time", "instances": 18, "metric_value": 1.0, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[14]>1.0:
					# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[5]>0:
							# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[16]<=1:
									return 'True'
								elif obj[16]>1:
									return 'False'
								else: return 'False'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						elif obj[5]<=0:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[14]<=1.0:
					return 'False'
				else: return 'False'
			elif obj[2]>2:
				# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[12]>0.0:
					return 'True'
				elif obj[12]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	else: return 'True'
