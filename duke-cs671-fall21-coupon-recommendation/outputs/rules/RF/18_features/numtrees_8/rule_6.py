def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9924, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Coupon_validity", "instances": 85, "metric_value": 0.9919, "depth": 2}
		if obj[4]<=0:
			# {"feature": "Bar", "instances": 52, "metric_value": 0.9732, "depth": 3}
			if obj[12]<=1.0:
				# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 4}
				if obj[3]>0:
					# {"feature": "Maritalstatus", "instances": 23, "metric_value": 0.9877, "depth": 5}
					if obj[7]<=2:
						# {"feature": "Income", "instances": 20, "metric_value": 1.0, "depth": 6}
						if obj[11]>3:
							# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=6:
								# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 8}
								if obj[9]<=1:
									# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[10]>2:
										# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[5]<=0:
											return 'True'
										elif obj[5]>0:
											# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[13]>0.0:
												return 'False'
											elif obj[13]<=0.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[10]<=2:
										return 'False'
									else: return 'False'
								elif obj[9]>1:
									return 'True'
								else: return 'True'
							elif obj[6]>6:
								return 'False'
							else: return 'False'
						elif obj[11]<=3:
							# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[13]<=0.0:
								return 'False'
							elif obj[13]>0.0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]<=2:
									return 'True'
								elif obj[2]>2:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[7]>2:
						return 'True'
					else: return 'True'
				elif obj[3]<=0:
					# {"feature": "Age", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[6]>1:
						return 'False'
					elif obj[6]<=1:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[15]>0.0:
							return 'True'
						elif obj[15]<=0.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[12]>1.0:
				# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.5033, "depth": 4}
				if obj[15]>0.0:
					return 'True'
				elif obj[15]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>0:
			# {"feature": "Occupation", "instances": 33, "metric_value": 0.7455, "depth": 3}
			if obj[10]<=7:
				# {"feature": "Income", "instances": 25, "metric_value": 0.8555, "depth": 4}
				if obj[11]<=7:
					# {"feature": "Time", "instances": 23, "metric_value": 0.7554, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.4855, "depth": 6}
						if obj[15]<=1.0:
							return 'False'
						elif obj[15]>1.0:
							# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[13]>1.0:
								return 'False'
							elif obj[13]<=1.0:
								# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[1]<=0:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]<=1:
										return 'False'
									elif obj[6]>1:
										return 'True'
									else: return 'True'
								elif obj[1]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[2]>3:
						# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]<=0:
							return 'True'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[11]>7:
					return 'True'
				else: return 'True'
			elif obj[10]>7:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Bar", "instances": 42, "metric_value": 0.7919, "depth": 2}
		if obj[12]<=1.0:
			# {"feature": "Education", "instances": 34, "metric_value": 0.874, "depth": 3}
			if obj[9]>1:
				# {"feature": "Coupon", "instances": 19, "metric_value": 0.9819, "depth": 4}
				if obj[3]>1:
					# {"feature": "Children", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[8]>0:
						return 'True'
					elif obj[8]<=0:
						# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[2]<=0:
							# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]>1:
								return 'True'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[2]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[9]<=1:
				# {"feature": "Coupon_validity", "instances": 15, "metric_value": 0.5665, "depth": 4}
				if obj[4]<=0:
					return 'True'
				elif obj[4]>0:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]>2:
						return 'True'
					elif obj[2]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[12]>1.0:
			return 'True'
		else: return 'True'
	else: return 'True'
