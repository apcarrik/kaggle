def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9978, "depth": 1}
	if obj[3]>1:
		# {"feature": "Coupon_validity", "instances": 92, "metric_value": 0.9583, "depth": 2}
		if obj[4]>0:
			# {"feature": "Weather", "instances": 49, "metric_value": 0.9973, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Bar", "instances": 37, "metric_value": 0.974, "depth": 4}
				if obj[11]<=1.0:
					# {"feature": "Occupation", "instances": 27, "metric_value": 0.999, "depth": 5}
					if obj[9]<=19:
						# {"feature": "Time", "instances": 25, "metric_value": 0.9988, "depth": 6}
						if obj[2]>0:
							# {"feature": "Income", "instances": 16, "metric_value": 0.9544, "depth": 7}
							if obj[10]<=5:
								# {"feature": "Gender", "instances": 12, "metric_value": 1.0, "depth": 8}
								if obj[5]>0:
									# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[15]>1:
										return 'False'
									elif obj[15]<=1:
										# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[0]>1:
											return 'True'
										elif obj[0]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[5]<=0:
									# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[6]<=3:
										return 'True'
									elif obj[6]>3:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]<=2:
											return 'True'
										elif obj[0]>2:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[10]>5:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							# {"feature": "Age", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[6]>3:
								return 'True'
							elif obj[6]<=3:
								# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[12]<=3.0:
										return 'False'
									elif obj[12]>3.0:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[9]>19:
						return 'False'
					else: return 'False'
				elif obj[11]>1.0:
					# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[12]>0.0:
						return 'True'
					elif obj[12]<=0.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[1]>0:
				# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[6]<=6:
					return 'False'
				elif obj[6]>6:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]>1:
						return 'False'
					elif obj[2]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[4]<=0:
			# {"feature": "Occupation", "instances": 43, "metric_value": 0.7401, "depth": 3}
			if obj[9]<=11:
				# {"feature": "Coffeehouse", "instances": 32, "metric_value": 0.4489, "depth": 4}
				if obj[12]>1.0:
					return 'True'
				elif obj[12]<=1.0:
					# {"feature": "Time", "instances": 15, "metric_value": 0.7219, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[11]<=0.0:
							# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[5]>0:
								# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[7]<=0:
									return 'True'
								elif obj[7]>0:
									return 'False'
								else: return 'False'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[11]>0.0:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[9]>11:
				# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[12]<=3.0:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[11]<=0.0:
						# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[15]<=1:
							# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[8]<=2:
								return 'False'
							elif obj[8]>2:
								return 'True'
							else: return 'True'
						elif obj[15]>1:
							return 'True'
						else: return 'True'
					elif obj[11]>0.0:
						return 'False'
					else: return 'False'
				elif obj[12]>3.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Income", "instances": 35, "metric_value": 0.8631, "depth": 2}
		if obj[10]>0:
			# {"feature": "Coffeehouse", "instances": 33, "metric_value": 0.799, "depth": 3}
			if obj[12]>0.0:
				# {"feature": "Age", "instances": 23, "metric_value": 0.5586, "depth": 4}
				if obj[6]>1:
					return 'False'
				elif obj[6]<=1:
					# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[9]<=6:
								return 'False'
							elif obj[9]>6:
								return 'True'
							else: return 'True'
						elif obj[7]>0:
							return 'True'
						else: return 'True'
					elif obj[5]>0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[12]<=0.0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[9]>1:
					# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[8]>0:
						return 'False'
					elif obj[8]<=0:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
