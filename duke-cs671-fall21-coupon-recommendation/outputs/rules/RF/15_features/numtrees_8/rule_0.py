def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9964, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Coupon_validity", "instances": 72, "metric_value": 0.9641, "depth": 2}
		if obj[3]<=0:
			# {"feature": "Bar", "instances": 39, "metric_value": 0.9995, "depth": 3}
			if obj[10]<=1.0:
				# {"feature": "Coupon", "instances": 29, "metric_value": 0.9576, "depth": 4}
				if obj[2]>1:
					# {"feature": "Income", "instances": 16, "metric_value": 0.9887, "depth": 5}
					if obj[9]>3:
						# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[5]<=4:
							return 'True'
						elif obj[5]>4:
							return 'False'
						else: return 'False'
					elif obj[9]<=3:
						# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[14]>1:
							return 'False'
						elif obj[14]<=1:
							# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]>0:
								return 'True'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=1:
					# {"feature": "Children", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[6]<=0:
						return 'False'
					elif obj[6]>0:
						# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]<=0:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=2:
								return 'True'
							elif obj[5]>2:
								return 'False'
							else: return 'False'
						elif obj[4]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[10]>1.0:
				# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[5]<=4:
					return 'True'
				elif obj[5]>4:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>0:
			# {"feature": "Education", "instances": 33, "metric_value": 0.799, "depth": 3}
			if obj[7]<=3:
				# {"feature": "Age", "instances": 31, "metric_value": 0.7088, "depth": 4}
				if obj[5]>2:
					# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.8454, "depth": 5}
					if obj[12]>0.0:
						# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9367, "depth": 6}
						if obj[11]>0.0:
							# {"feature": "Income", "instances": 14, "metric_value": 0.9852, "depth": 7}
							if obj[9]<=3:
								# {"feature": "Bar", "instances": 12, "metric_value": 0.9183, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[2]>2:
										# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=6:
											return 'True'
										elif obj[8]>6:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[13]<=0:
												return 'False'
											elif obj[13]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[2]<=2:
										return 'False'
									else: return 'False'
								elif obj[10]>1.0:
									return 'False'
								else: return 'False'
							elif obj[9]>3:
								return 'True'
							else: return 'True'
						elif obj[11]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[12]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[5]<=2:
					return 'False'
				else: return 'False'
			elif obj[7]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Income", "instances": 55, "metric_value": 0.8454, "depth": 2}
		if obj[9]>0:
			# {"feature": "Coupon", "instances": 47, "metric_value": 0.7046, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coffeehouse", "instances": 44, "metric_value": 0.6321, "depth": 4}
				if obj[11]>0.0:
					# {"feature": "Age", "instances": 35, "metric_value": 0.7219, "depth": 5}
					if obj[5]<=4:
						# {"feature": "Children", "instances": 28, "metric_value": 0.5917, "depth": 6}
						if obj[6]>0:
							# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 7}
							if obj[10]<=1.0:
								# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 8}
								if obj[7]<=2:
									return 'True'
								elif obj[7]>2:
									# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]>0:
										return 'True'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[10]>1.0:
								# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]>0:
										return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					elif obj[5]>4:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[8]>2:
							# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[1]<=3:
								return 'True'
							elif obj[1]>3:
								return 'False'
							else: return 'False'
						elif obj[8]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[11]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=0:
					return 'False'
				elif obj[3]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]<=0:
			# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[14]>1:
				return 'False'
			elif obj[14]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
