def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon_validity", "instances": 127, "metric_value": 0.9924, "depth": 1}
	if obj[4]<=0:
		# {"feature": "Coupon", "instances": 77, "metric_value": 0.9457, "depth": 2}
		if obj[3]>1:
			# {"feature": "Time", "instances": 42, "metric_value": 0.7025, "depth": 3}
			if obj[2]>0:
				# {"feature": "Income", "instances": 32, "metric_value": 0.5436, "depth": 4}
				if obj[10]<=4:
					return 'True'
				elif obj[10]>4:
					# {"feature": "Passanger", "instances": 15, "metric_value": 0.8366, "depth": 5}
					if obj[0]>1:
						# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[15]<=1:
							# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'True'
							else: return 'True'
						elif obj[15]>1:
							return 'True'
						else: return 'True'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Children", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[7]>0:
					# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[5]>0:
						return 'False'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				elif obj[7]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]<=1:
			# {"feature": "Bar", "instances": 35, "metric_value": 0.9852, "depth": 3}
			if obj[11]<=0.0:
				# {"feature": "Education", "instances": 18, "metric_value": 0.65, "depth": 4}
				if obj[8]>0:
					return 'False'
				elif obj[8]<=0:
					# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[12]<=1.0:
						# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[10]<=4:
							return 'False'
						elif obj[10]>4:
							return 'True'
						else: return 'True'
					elif obj[12]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[11]>0.0:
				# {"feature": "Gender", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[5]>0:
					# {"feature": "Income", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[10]>1:
						# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[2]>0:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[13]>1.0:
									# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]>0:
										return 'True'
									elif obj[8]<=0:
										return 'False'
									else: return 'False'
								elif obj[13]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[10]<=1:
						return 'False'
					else: return 'False'
				elif obj[5]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]>0:
		# {"feature": "Income", "instances": 50, "metric_value": 0.9815, "depth": 2}
		if obj[10]<=6:
			# {"feature": "Education", "instances": 44, "metric_value": 0.9457, "depth": 3}
			if obj[8]<=2:
				# {"feature": "Coupon", "instances": 33, "metric_value": 0.994, "depth": 4}
				if obj[3]>3:
					# {"feature": "Occupation", "instances": 17, "metric_value": 0.7871, "depth": 5}
					if obj[9]>0:
						# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.6962, "depth": 6}
						if obj[12]>-1.0:
							# {"feature": "Gender", "instances": 15, "metric_value": 0.5665, "depth": 7}
							if obj[5]>0:
								# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[2]>1:
									return 'False'
								elif obj[2]<=1:
									# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[12]<=-1.0:
							return 'True'
						else: return 'True'
					elif obj[9]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]<=3:
					# {"feature": "Time", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[2]>2:
						# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[9]<=12:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[13]>0.0:
								return 'True'
							elif obj[13]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[9]>12:
							return 'False'
						else: return 'False'
					elif obj[2]<=2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[8]>2:
				# {"feature": "Age", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[6]<=3:
					return 'False'
				elif obj[6]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]>6:
			# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[11]<=2.0:
				return 'True'
			elif obj[11]>2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
