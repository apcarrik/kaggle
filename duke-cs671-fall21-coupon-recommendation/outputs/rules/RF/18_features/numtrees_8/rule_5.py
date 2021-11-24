def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coffeehouse", "instances": 127, "metric_value": 0.9978, "depth": 1}
	if obj[13]<=1.0:
		# {"feature": "Education", "instances": 65, "metric_value": 0.9612, "depth": 2}
		if obj[9]<=3:
			# {"feature": "Coupon_validity", "instances": 57, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Coupon", "instances": 31, "metric_value": 0.9932, "depth": 4}
				if obj[3]>1:
					# {"feature": "Passanger", "instances": 19, "metric_value": 0.9495, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Age", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[6]>1:
							# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[10]<=7:
								# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[2]<=1:
									# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[15]<=0.0:
										# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7]<=1:
											return 'True'
										elif obj[7]>1:
											return 'False'
										else: return 'False'
									elif obj[15]>0.0:
										return 'False'
									else: return 'False'
								elif obj[2]>1:
									return 'True'
								else: return 'True'
							elif obj[10]>7:
								return 'False'
							else: return 'False'
						elif obj[6]<=1:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[3]<=1:
					# {"feature": "Income", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[11]>1:
						return 'False'
					elif obj[11]<=1:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[10]<=5:
							return 'True'
						elif obj[10]>5:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[4]>0:
				# {"feature": "Income", "instances": 26, "metric_value": 0.7063, "depth": 4}
				if obj[11]<=3:
					return 'False'
				elif obj[11]>3:
					# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[16]<=0:
						# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[10]<=11:
							return 'False'
						elif obj[10]>11:
							return 'True'
						else: return 'True'
					elif obj[16]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[9]>3:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[3]>1:
				return 'True'
			elif obj[3]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[13]>1.0:
		# {"feature": "Education", "instances": 62, "metric_value": 0.9072, "depth": 2}
		if obj[9]>0:
			# {"feature": "Occupation", "instances": 38, "metric_value": 0.992, "depth": 3}
			if obj[10]<=10:
				# {"feature": "Weather", "instances": 28, "metric_value": 0.9852, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Coupon", "instances": 24, "metric_value": 1.0, "depth": 5}
					if obj[3]<=3:
						# {"feature": "Restaurantlessthan20", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[14]<=2.0:
							# {"feature": "Gender", "instances": 10, "metric_value": 0.469, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]>1:
									return 'True'
								elif obj[0]<=1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[14]>2.0:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]>3:
						# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=1:
							return 'False'
						elif obj[2]>1:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>0:
								return 'True'
							elif obj[6]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			elif obj[10]>10:
				# {"feature": "Time", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]<=0:
			# {"feature": "Income", "instances": 24, "metric_value": 0.5436, "depth": 3}
			if obj[11]<=7:
				# {"feature": "Time", "instances": 21, "metric_value": 0.2762, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=2:
						return 'True'
					elif obj[3]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[11]>7:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>1:
					return 'False'
				elif obj[2]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'True'
