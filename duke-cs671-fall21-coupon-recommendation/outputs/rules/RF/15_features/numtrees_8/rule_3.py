def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Education", "instances": 127, "metric_value": 0.9924, "depth": 1}
	if obj[7]<=2:
		# {"feature": "Coupon", "instances": 96, "metric_value": 0.9464, "depth": 2}
		if obj[2]>1:
			# {"feature": "Restaurant20to50", "instances": 65, "metric_value": 0.8717, "depth": 3}
			if obj[12]<=2.0:
				# {"feature": "Coupon_validity", "instances": 59, "metric_value": 0.9066, "depth": 4}
				if obj[3]>0:
					# {"feature": "Distance", "instances": 30, "metric_value": 0.9871, "depth": 5}
					if obj[14]<=2:
						# {"feature": "Time", "instances": 27, "metric_value": 0.951, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Income", "instances": 14, "metric_value": 0.9852, "depth": 7}
							if obj[9]>1:
								# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=1:
									# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[8]<=4:
										# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[10]>0.0:
											return 'True'
										elif obj[10]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[8]>4:
										return 'False'
									else: return 'False'
								elif obj[5]>1:
									return 'True'
								else: return 'True'
							elif obj[9]<=1:
								return 'False'
							else: return 'False'
						elif obj[1]>2:
							# {"feature": "Bar", "instances": 13, "metric_value": 0.6194, "depth": 7}
							if obj[10]<=1.0:
								# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 8}
								if obj[5]<=4:
									return 'True'
								elif obj[5]>4:
									# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[4]<=0:
										return 'True'
									elif obj[4]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[10]>1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[14]>2:
						return 'False'
					else: return 'False'
				elif obj[3]<=0:
					# {"feature": "Coffeehouse", "instances": 29, "metric_value": 0.7355, "depth": 5}
					if obj[11]<=1.0:
						# {"feature": "Passanger", "instances": 17, "metric_value": 0.9367, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Direction_same", "instances": 12, "metric_value": 1.0, "depth": 7}
							if obj[13]<=0:
								# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[8]>1:
									# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[5]<=4:
										return 'False'
									elif obj[5]>4:
										# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1]<=1:
											return 'False'
										elif obj[1]>1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]<=1:
									return 'True'
								else: return 'True'
							elif obj[13]>0:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[11]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[12]>2.0:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Bar", "instances": 31, "metric_value": 0.9992, "depth": 3}
			if obj[10]>0.0:
				# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[11]>0.0:
					# {"feature": "Income", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[9]>1:
						# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[5]>1:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]<=3:
									return 'False'
								elif obj[1]>3:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[5]<=1:
							return 'True'
						else: return 'True'
					elif obj[9]<=1:
						return 'False'
					else: return 'False'
				elif obj[11]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[10]<=0.0:
				# {"feature": "Age", "instances": 15, "metric_value": 0.8366, "depth": 4}
				if obj[5]<=4:
					# {"feature": "Income", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[9]<=5:
						return 'False'
					elif obj[9]>5:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[8]<=4:
							return 'False'
						elif obj[8]>4:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]>4:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[7]>2:
		# {"feature": "Coupon", "instances": 31, "metric_value": 0.8691, "depth": 2}
		if obj[2]>1:
			# {"feature": "Coupon_validity", "instances": 20, "metric_value": 0.9928, "depth": 3}
			if obj[3]<=0:
				# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[9]<=4:
						return 'False'
					elif obj[9]>4:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			elif obj[3]>0:
				# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[5]>2:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[14]>1:
						return 'False'
					elif obj[14]<=1:
						return 'True'
					else: return 'True'
				elif obj[5]<=2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
