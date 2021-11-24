def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9802, "depth": 1}
	if obj[3]>1:
		# {"feature": "Gender", "instances": 95, "metric_value": 0.8997, "depth": 2}
		if obj[5]<=0:
			# {"feature": "Occupation", "instances": 54, "metric_value": 0.9751, "depth": 3}
			if obj[9]<=9:
				# {"feature": "Time", "instances": 34, "metric_value": 0.8338, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Age", "instances": 28, "metric_value": 0.9059, "depth": 5}
					if obj[6]>0:
						# {"feature": "Coupon_validity", "instances": 24, "metric_value": 0.9544, "depth": 6}
						if obj[4]<=0:
							# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.7793, "depth": 7}
							if obj[12]<=1.0:
								# {"feature": "Income", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[10]>0:
									# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[13]>0.0:
										# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[1]<=1:
											return 'False'
										elif obj[1]>1:
											return 'True'
										else: return 'True'
									elif obj[13]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[10]<=0:
									return 'True'
								else: return 'True'
							elif obj[12]>1.0:
								return 'True'
							else: return 'True'
						elif obj[4]>0:
							# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[12]>0.0:
								# {"feature": "Weather", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[1]<=0:
									# {"feature": "Children", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[8]>1:
											return 'False'
										elif obj[8]<=1:
											return 'True'
										else: return 'True'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[1]>0:
									return 'False'
								else: return 'False'
							elif obj[12]<=0.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]<=0:
						return 'True'
					else: return 'True'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[9]>9:
				# {"feature": "Time", "instances": 20, "metric_value": 0.9341, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Distance", "instances": 15, "metric_value": 0.9968, "depth": 5}
					if obj[15]<=2:
						# {"feature": "Age", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[6]>2:
							# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[11]<=1.0:
								# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[12]>0.0:
										return 'False'
									elif obj[12]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							elif obj[11]>1.0:
								return 'True'
							else: return 'True'
						elif obj[6]<=2:
							# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[10]>2:
								return 'False'
							elif obj[10]<=2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[15]>2:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[5]>0:
			# {"feature": "Income", "instances": 41, "metric_value": 0.7121, "depth": 3}
			if obj[10]>2:
				# {"feature": "Weather", "instances": 30, "metric_value": 0.469, "depth": 4}
				if obj[1]<=0:
					# {"feature": "Age", "instances": 24, "metric_value": 0.2499, "depth": 5}
					if obj[6]<=5:
						return 'True'
					elif obj[6]>5:
						# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]>0:
					# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[2]>1:
						# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>0:
							return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[10]<=2:
				# {"feature": "Age", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[6]>2:
					# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[2]<=1:
						return 'False'
					elif obj[2]>1:
						# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[8]>2:
							return 'True'
						elif obj[8]<=2:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[6]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Weather", "instances": 32, "metric_value": 0.8571, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Age", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[6]<=5:
				# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.9495, "depth": 4}
				if obj[12]>0.0:
					# {"feature": "Income", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[10]>1:
						return 'False'
					elif obj[10]<=1:
						# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=0:
							return 'True'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[12]<=0.0:
					# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[2]>0:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[13]<=1.0:
							return 'False'
						elif obj[13]>1.0:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[6]>5:
				return 'True'
			else: return 'True'
		elif obj[1]>0:
			return 'False'
		else: return 'False'
	else: return 'False'
