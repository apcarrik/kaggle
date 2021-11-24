def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Age", "instances": 127, "metric_value": 0.9899, "depth": 1}
	if obj[6]<=3:
		# {"feature": "Distance", "instances": 64, "metric_value": 0.8774, "depth": 2}
		if obj[17]<=2:
			# {"feature": "Coupon", "instances": 56, "metric_value": 0.9241, "depth": 3}
			if obj[3]>0:
				# {"feature": "Coupon_validity", "instances": 45, "metric_value": 0.971, "depth": 4}
				if obj[4]>0:
					# {"feature": "Restaurantlessthan20", "instances": 24, "metric_value": 0.7383, "depth": 5}
					if obj[14]>0.0:
						# {"feature": "Gender", "instances": 23, "metric_value": 0.6666, "depth": 6}
						if obj[5]>0:
							# {"feature": "Income", "instances": 12, "metric_value": 0.9183, "depth": 7}
							if obj[11]>1:
								# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[13]<=1.0:
									# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[10]>5:
										return 'False'
									elif obj[10]<=5:
										# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[2]>0:
											return 'True'
										elif obj[2]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[13]>1.0:
									return 'True'
								else: return 'True'
							elif obj[11]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]<=0:
							return 'False'
						else: return 'False'
					elif obj[14]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[4]<=0:
					# {"feature": "Education", "instances": 21, "metric_value": 0.9587, "depth": 5}
					if obj[9]<=1:
						# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[12]<=1.0:
							# {"feature": "Weather", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[2]<=2:
									return 'True'
								elif obj[2]>2:
									return 'False'
								else: return 'False'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						elif obj[12]>1.0:
							return 'False'
						else: return 'False'
					elif obj[9]>1:
						# {"feature": "Income", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[11]<=4:
							return 'True'
						elif obj[11]>4:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[3]<=0:
				# {"feature": "Bar", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[12]<=1.0:
					return 'False'
				elif obj[12]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[17]>2:
			return 'False'
		else: return 'False'
	elif obj[6]>3:
		# {"feature": "Coffeehouse", "instances": 63, "metric_value": 0.9779, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Bar", "instances": 47, "metric_value": 0.8787, "depth": 3}
			if obj[12]>0.0:
				# {"feature": "Distance", "instances": 29, "metric_value": 0.5788, "depth": 4}
				if obj[17]<=2:
					# {"feature": "Restaurantlessthan20", "instances": 26, "metric_value": 0.3912, "depth": 5}
					if obj[14]>1.0:
						return 'True'
					elif obj[14]<=1.0:
						# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[3]>2:
							return 'True'
						elif obj[3]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[17]>2:
					# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[11]>0:
						return 'False'
					elif obj[11]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[12]<=0.0:
				# {"feature": "Coupon", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[3]>0:
					# {"feature": "Income", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[11]<=3:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[11]>3:
						# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[1]<=0:
							return 'True'
						elif obj[1]>0:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]>0:
									return 'False'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[13]<=0.0:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[10]<=8:
				# {"feature": "Income", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[11]>1:
					# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[2]>1:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[15]<=0.0:
							return 'True'
						elif obj[15]>0.0:
							return 'False'
						else: return 'False'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				elif obj[11]<=1:
					return 'True'
				else: return 'True'
			elif obj[10]>8:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
