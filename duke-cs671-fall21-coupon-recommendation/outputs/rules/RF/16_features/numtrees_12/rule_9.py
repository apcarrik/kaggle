def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9831, "depth": 1}
	if obj[3]>1:
		# {"feature": "Passanger", "instances": 62, "metric_value": 0.9236, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Income", "instances": 35, "metric_value": 0.9947, "depth": 3}
			if obj[10]<=6:
				# {"feature": "Time", "instances": 29, "metric_value": 0.9923, "depth": 4}
				if obj[2]>0:
					# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.9751, "depth": 5}
					if obj[13]<=3.0:
						# {"feature": "Coupon_validity", "instances": 25, "metric_value": 0.9427, "depth": 6}
						if obj[4]>0:
							# {"feature": "Education", "instances": 14, "metric_value": 0.7496, "depth": 7}
							if obj[8]>1:
								return 'False'
							elif obj[8]<=1:
								# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[14]<=0:
									return 'False'
								elif obj[14]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]<=0:
							# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[11]<=1.0:
								# {"feature": "Gender", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[6]>1:
										# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[12]<=1.0:
											return 'False'
										elif obj[12]>1.0:
											return 'True'
										else: return 'True'
									elif obj[6]<=1:
										return 'True'
									else: return 'True'
								elif obj[5]>0:
									return 'True'
								else: return 'True'
							elif obj[11]>1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[13]>3.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			elif obj[10]>6:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Age", "instances": 27, "metric_value": 0.6913, "depth": 3}
			if obj[6]>2:
				return 'True'
			elif obj[6]<=2:
				# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[2]>0:
					# {"feature": "Income", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[10]<=4:
						# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[9]<=21:
							return 'True'
						elif obj[9]>21:
							return 'False'
						else: return 'False'
					elif obj[10]>4:
						return 'False'
					else: return 'False'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Education", "instances": 23, "metric_value": 0.9321, "depth": 2}
		if obj[8]<=3:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.8631, "depth": 3}
			if obj[9]<=8:
				# {"feature": "Passanger", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[6]<=1:
						return 'True'
					elif obj[6]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]>8:
				# {"feature": "Gender", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[5]>0:
					# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[5]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[8]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
