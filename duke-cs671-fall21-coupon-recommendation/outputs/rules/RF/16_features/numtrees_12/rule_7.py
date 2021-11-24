def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[8]<=3:
		# {"feature": "Age", "instances": 77, "metric_value": 0.994, "depth": 2}
		if obj[6]>0:
			# {"feature": "Coupon_validity", "instances": 67, "metric_value": 0.9727, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Occupation", "instances": 36, "metric_value": 0.8524, "depth": 4}
				if obj[9]<=11:
					# {"feature": "Income", "instances": 28, "metric_value": 0.9403, "depth": 5}
					if obj[10]<=6:
						# {"feature": "Coupon", "instances": 24, "metric_value": 0.9799, "depth": 6}
						if obj[3]<=3:
							# {"feature": "Passanger", "instances": 18, "metric_value": 0.8524, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Distance", "instances": 14, "metric_value": 0.9403, "depth": 8}
								if obj[15]<=1:
									# {"feature": "Gender", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[5]>0:
										return 'True'
									elif obj[5]<=0:
										# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[2]<=0:
											return 'True'
										elif obj[2]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[15]>1:
									# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[12]>0.0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[5]>0:
											return 'False'
										elif obj[5]<=0:
											# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[2]>0:
												return 'True'
											elif obj[2]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[12]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						elif obj[3]>3:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[10]>6:
						return 'True'
					else: return 'True'
				elif obj[9]>11:
					return 'True'
				else: return 'True'
			elif obj[4]>0:
				# {"feature": "Coupon", "instances": 31, "metric_value": 0.9932, "depth": 4}
				if obj[3]>2:
					# {"feature": "Occupation", "instances": 20, "metric_value": 0.971, "depth": 5}
					if obj[9]<=11:
						# {"feature": "Time", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[13]>0.0:
								# {"feature": "Weather", "instances": 10, "metric_value": 0.8813, "depth": 8}
								if obj[1]<=0:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[14]<=0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[5]<=0:
											return 'False'
										elif obj[5]>0:
											# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=2:
												return 'False'
											elif obj[10]>2:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[14]>0:
										# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[12]<=2.0:
											return 'True'
										elif obj[12]>2.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[1]>0:
									return 'False'
								else: return 'False'
							elif obj[13]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[2]>3:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]>0:
									return 'True'
								elif obj[7]<=0:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[9]>11:
						return 'True'
					else: return 'True'
				elif obj[3]<=2:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[11]>0.0:
						return 'False'
					elif obj[11]<=0.0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[9]<=6:
								return 'True'
							elif obj[9]>6:
								return 'False'
							else: return 'False'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[6]<=0:
			# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[13]>0.0:
				return 'False'
			elif obj[13]<=0.0:
				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[8]>3:
		return 'True'
	else: return 'True'
