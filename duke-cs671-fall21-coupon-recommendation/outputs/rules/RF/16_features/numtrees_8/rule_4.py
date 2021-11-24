def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Education", "instances": 127, "metric_value": 0.9802, "depth": 1}
	if obj[8]>0:
		# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.9999, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Coupon_validity", "instances": 74, "metric_value": 0.9953, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Occupation", "instances": 37, "metric_value": 0.909, "depth": 4}
				if obj[9]<=11:
					# {"feature": "Gender", "instances": 27, "metric_value": 0.7642, "depth": 5}
					if obj[5]>0:
						# {"feature": "Age", "instances": 16, "metric_value": 0.9544, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Time", "instances": 12, "metric_value": 1.0, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Weather", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[1]<=0:
										return 'True'
									elif obj[1]>0:
										# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7]>0:
											return 'False'
										elif obj[7]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]>3:
									return 'False'
								else: return 'False'
							elif obj[2]>2:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
							return 'True'
						else: return 'True'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				elif obj[9]>11:
					# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[11]<=2.0:
						# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[3]<=2:
							return 'False'
						elif obj[3]>2:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[14]<=0:
								return 'True'
							elif obj[14]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[11]>2.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>0:
				# {"feature": "Income", "instances": 37, "metric_value": 0.974, "depth": 4}
				if obj[10]>1:
					# {"feature": "Passanger", "instances": 31, "metric_value": 0.9992, "depth": 5}
					if obj[0]>0:
						# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.9852, "depth": 6}
						if obj[12]>0.0:
							# {"feature": "Age", "instances": 21, "metric_value": 0.9852, "depth": 7}
							if obj[6]>0:
								# {"feature": "Time", "instances": 17, "metric_value": 0.9975, "depth": 8}
								if obj[2]<=1:
									# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 9}
									if obj[3]<=3:
										# {"feature": "Bar", "instances": 8, "metric_value": 0.5436, "depth": 10}
										if obj[11]<=1.0:
											return 'True'
										elif obj[11]>1.0:
											return 'False'
										else: return 'False'
									elif obj[3]>3:
										return 'False'
									else: return 'False'
								elif obj[2]>1:
									# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[7]>0:
										return 'False'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						elif obj[12]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				elif obj[10]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[13]<=0.0:
			# {"feature": "Passanger", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[0]>0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[9]>5:
					return 'False'
				elif obj[9]<=5:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]<=1:
						return 'False'
					elif obj[2]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[8]<=0:
		# {"feature": "Time", "instances": 42, "metric_value": 0.7919, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Coupon", "instances": 30, "metric_value": 0.9183, "depth": 3}
			if obj[3]>1:
				# {"feature": "Income", "instances": 23, "metric_value": 0.7554, "depth": 4}
				if obj[10]<=7:
					# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[13]<=1.0:
						# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[9]<=10:
							# {"feature": "Weather", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[11]<=1.0:
									return 'True'
								elif obj[11]>1.0:
									# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[0]>1:
										# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6]>0:
											return 'True'
										elif obj[6]<=0:
											return 'False'
										else: return 'False'
									elif obj[0]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						elif obj[9]>10:
							return 'False'
						else: return 'False'
					elif obj[13]>1.0:
						return 'True'
					else: return 'True'
				elif obj[10]>7:
					return 'True'
				else: return 'True'
			elif obj[3]<=1:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[9]>6:
					return 'False'
				elif obj[9]<=6:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>3:
			return 'True'
		else: return 'True'
	else: return 'True'
