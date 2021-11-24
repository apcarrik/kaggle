def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[14]<=2.0:
		# {"feature": "Passanger", "instances": 78, "metric_value": 0.9881, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Income", "instances": 51, "metric_value": 0.9367, "depth": 3}
			if obj[11]>2:
				# {"feature": "Bar", "instances": 36, "metric_value": 0.9978, "depth": 4}
				if obj[12]<=2.0:
					# {"feature": "Coupon_validity", "instances": 32, "metric_value": 0.9745, "depth": 5}
					if obj[4]<=0:
						# {"feature": "Education", "instances": 18, "metric_value": 0.7642, "depth": 6}
						if obj[9]>1:
							# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[10]>5:
								# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[6]>0:
									return 'False'
								elif obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[10]<=5:
								# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]>0:
									return 'True'
								elif obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[9]<=1:
							return 'False'
						else: return 'False'
					elif obj[4]>0:
						# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[13]<=1.0:
							# {"feature": "Maritalstatus", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[7]<=1:
								# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[10]<=10:
									return 'False'
								elif obj[10]>10:
									# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]>0:
										return 'True'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[7]>1:
								# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[2]>0:
									return 'True'
								elif obj[2]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[13]>1.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[12]>2.0:
					return 'True'
				else: return 'True'
			elif obj[11]<=2:
				# {"feature": "Age", "instances": 15, "metric_value": 0.3534, "depth": 4}
				if obj[6]<=6:
					return 'False'
				elif obj[6]>6:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[0]>1:
			# {"feature": "Age", "instances": 27, "metric_value": 0.9751, "depth": 3}
			if obj[6]<=3:
				# {"feature": "Children", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[8]>0:
					# {"feature": "Occupation", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[10]<=10:
						# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[1]<=0:
							return 'True'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					elif obj[10]>10:
						# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=0:
							# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[2]<=2:
								return 'False'
							elif obj[2]>2:
								# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]<=1:
									return 'True'
								elif obj[3]>1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[8]<=0:
					return 'True'
				else: return 'True'
			elif obj[6]>3:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[10]<=9:
					# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[4]>0:
						return 'False'
					elif obj[4]<=0:
						# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[7]<=0:
							return 'True'
						elif obj[7]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[10]>9:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[14]>2.0:
		# {"feature": "Income", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[11]>0:
			return 'True'
		elif obj[11]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
