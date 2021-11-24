def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[3]>1:
		# {"feature": "Education", "instances": 54, "metric_value": 0.8256, "depth": 2}
		if obj[8]>1:
			# {"feature": "Distance", "instances": 32, "metric_value": 0.9544, "depth": 3}
			if obj[15]<=2:
				# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.8936, "depth": 4}
				if obj[13]>1.0:
					# {"feature": "Occupation", "instances": 15, "metric_value": 0.5665, "depth": 5}
					if obj[9]<=12:
						return 'True'
					elif obj[9]>12:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[13]<=1.0:
					# {"feature": "Coffeehouse", "instances": 14, "metric_value": 1.0, "depth": 5}
					if obj[12]>1.0:
						# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0:
								return 'True'
							elif obj[4]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[12]<=1.0:
						# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[5]>0:
							return 'False'
						elif obj[5]<=0:
							# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[9]<=7:
								return 'True'
							elif obj[9]>7:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[15]>2:
				return 'False'
			else: return 'False'
		elif obj[8]<=1:
			# {"feature": "Age", "instances": 22, "metric_value": 0.4395, "depth": 3}
			if obj[6]<=5:
				return 'True'
			elif obj[6]>5:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[15]<=2:
					# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[7]>0:
						return 'True'
					elif obj[7]<=0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'True'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[15]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Coupon_validity", "instances": 31, "metric_value": 0.9072, "depth": 2}
		if obj[4]<=0:
			# {"feature": "Income", "instances": 24, "metric_value": 0.9799, "depth": 3}
			if obj[10]>2:
				# {"feature": "Age", "instances": 18, "metric_value": 0.8524, "depth": 4}
				if obj[6]<=4:
					# {"feature": "Bar", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[11]>0.0:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[9]<=17:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[13]>1.0:
								return 'False'
							elif obj[13]<=1.0:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]>0:
									return 'True'
								elif obj[5]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[9]>17:
							return 'True'
						else: return 'True'
					elif obj[11]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[6]>4:
					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[10]<=2:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]>2:
						return 'False'
					elif obj[2]<=2:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[4]>0:
			return 'False'
		else: return 'False'
	else: return 'False'
