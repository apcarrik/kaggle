def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9978, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coupon_validity", "instances": 91, "metric_value": 0.9449, "depth": 2}
		if obj[3]>0:
			# {"feature": "Passanger", "instances": 51, "metric_value": 0.9931, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Income", "instances": 33, "metric_value": 0.9183, "depth": 4}
				if obj[9]<=5:
					# {"feature": "Time", "instances": 23, "metric_value": 0.7554, "depth": 5}
					if obj[1]>0:
						# {"feature": "Children", "instances": 17, "metric_value": 0.874, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.6194, "depth": 7}
							if obj[11]>0.0:
								return 'False'
							elif obj[11]<=0.0:
								# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[7]>1:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4]>0:
										# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]<=2:
											return 'False'
										elif obj[5]>2:
											return 'True'
										else: return 'True'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								elif obj[7]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[6]>0:
							# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[8]>4:
								return 'True'
							elif obj[8]<=4:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[9]>5:
					# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[11]<=1.0:
						# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[7]>0:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[7]<=0:
							return 'False'
						else: return 'False'
					elif obj[11]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Occupation", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[8]<=7:
					# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[1]>0:
						# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[4]>0:
							return 'False'
						elif obj[4]<=0:
							# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]>1:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]>0:
									return 'True'
								elif obj[7]<=0:
									return 'False'
								else: return 'False'
							elif obj[5]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[8]>7:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]<=0:
			# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 0.5436, "depth": 3}
			if obj[12]<=1.0:
				# {"feature": "Age", "instances": 28, "metric_value": 0.6769, "depth": 4}
				if obj[5]<=4:
					# {"feature": "Income", "instances": 22, "metric_value": 0.7732, "depth": 5}
					if obj[9]<=6:
						# {"feature": "Time", "instances": 19, "metric_value": 0.6292, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Occupation", "instances": 18, "metric_value": 0.5033, "depth": 7}
							if obj[8]<=6:
								return 'True'
							elif obj[8]>6:
								# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[7]>0:
									# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[11]>2.0:
										# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[14]>1:
											return 'True'
										elif obj[14]<=1:
											return 'False'
										else: return 'False'
									elif obj[11]<=2.0:
										return 'True'
									else: return 'True'
								elif obj[7]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]>3:
							return 'False'
						else: return 'False'
					elif obj[9]>6:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]>4:
					return 'True'
				else: return 'True'
			elif obj[12]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 36, "metric_value": 0.8113, "depth": 2}
		if obj[10]<=1.0:
			# {"feature": "Age", "instances": 27, "metric_value": 0.5033, "depth": 3}
			if obj[5]<=5:
				# {"feature": "Income", "instances": 21, "metric_value": 0.2762, "depth": 4}
				if obj[9]<=7:
					return 'False'
				elif obj[9]>7:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]>1:
						return 'False'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>5:
				# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]>1.0:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[7]>2:
							return 'True'
						elif obj[7]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]>0:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
