def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Bar", "instances": 95, "metric_value": 0.9903, "depth": 2}
		if obj[11]<=2.0:
			# {"feature": "Restaurant20to50", "instances": 87, "metric_value": 0.9723, "depth": 3}
			if obj[13]<=1.0:
				# {"feature": "Age", "instances": 55, "metric_value": 0.9998, "depth": 4}
				if obj[6]<=4:
					# {"feature": "Coupon_validity", "instances": 34, "metric_value": 0.9367, "depth": 5}
					if obj[4]<=0:
						# {"feature": "Coupon", "instances": 21, "metric_value": 0.7919, "depth": 6}
						if obj[3]>0:
							# {"feature": "Income", "instances": 13, "metric_value": 0.3912, "depth": 7}
							if obj[10]<=7:
								return 'True'
							elif obj[10]>7:
								# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=0:
									return 'True'
								elif obj[1]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[3]<=0:
							# {"feature": "Income", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[10]>2:
								# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[1]<=0:
									return 'False'
								elif obj[1]>0:
									return 'True'
								else: return 'True'
							elif obj[10]<=2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>0:
						# {"feature": "Income", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[10]<=5:
							# {"feature": "Direction_same", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[14]<=0:
								# {"feature": "Weather", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[1]<=0:
									# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[9]>6:
										# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[3]>0:
											# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[12]>1.0:
												return 'False'
											elif obj[12]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]<=6:
										return 'True'
									else: return 'True'
								elif obj[1]>0:
									return 'False'
								else: return 'False'
							elif obj[14]>0:
								return 'False'
							else: return 'False'
						elif obj[10]>5:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]>4:
					# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.8631, "depth": 5}
					if obj[12]>0.0:
						# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[9]<=7:
							# {"feature": "Weather", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=0:
								return 'True'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						elif obj[9]>7:
							return 'False'
						else: return 'False'
					elif obj[12]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[13]>1.0:
				# {"feature": "Time", "instances": 32, "metric_value": 0.7579, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.5159, "depth": 5}
					if obj[12]<=2.0:
						# {"feature": "Education", "instances": 16, "metric_value": 0.6962, "depth": 6}
						if obj[8]>0:
							# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[15]<=1:
								# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]<=0:
										return 'True'
									elif obj[1]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[15]>1:
								# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]>0:
									return 'True'
								elif obj[7]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[8]<=0:
							return 'False'
						else: return 'False'
					elif obj[12]>2.0:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]>2:
						# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[6]<=4:
							return 'True'
						elif obj[6]>4:
							return 'False'
						else: return 'False'
					elif obj[3]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[11]>2.0:
			# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[10]>0:
				return 'True'
			elif obj[10]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Time", "instances": 32, "metric_value": 0.8113, "depth": 2}
		if obj[2]>2:
			# {"feature": "Bar", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[11]<=1.0:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[9]<=12:
					# {"feature": "Weather", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[10]>0:
							return 'False'
						elif obj[10]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[9]>12:
					return 'True'
				else: return 'True'
			elif obj[11]>1.0:
				return 'True'
			else: return 'True'
		elif obj[2]<=2:
			# {"feature": "Age", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[6]>1:
				return 'True'
			elif obj[6]<=1:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[8]>2:
					return 'True'
				elif obj[8]<=2:
					# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[9]>5:
						return 'True'
					elif obj[9]<=5:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
