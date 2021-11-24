def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9831, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Age", "instances": 51, "metric_value": 0.9931, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Coupon", "instances": 28, "metric_value": 0.9059, "depth": 3}
			if obj[2]>0:
				# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.7554, "depth": 4}
				if obj[9]<=3.0:
					# {"feature": "Bar", "instances": 21, "metric_value": 0.5917, "depth": 5}
					if obj[7]>0.0:
						return 'False'
					elif obj[7]<=0.0:
						# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[5]>1:
							# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[6]>4:
								# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[1]<=0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[11]<=1:
										return 'False'
									elif obj[11]>1:
										return 'True'
									else: return 'True'
								elif obj[1]>0:
									return 'False'
								else: return 'False'
							elif obj[6]<=4:
								return 'True'
							else: return 'True'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[9]>3.0:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>2:
			# {"feature": "Time", "instances": 23, "metric_value": 0.9656, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 18, "metric_value": 1.0, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[7]>-1.0:
						# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[9]<=1.0:
							# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[5]>0:
								# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[6]>1:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[11]>1:
										return 'False'
									elif obj[11]<=1:
										return 'True'
									else: return 'True'
								elif obj[6]<=1:
									return 'True'
								else: return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[9]>1.0:
							return 'False'
						else: return 'False'
					elif obj[7]<=-1.0:
						return 'True'
					else: return 'True'
				elif obj[2]>2:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[11]<=1:
						return 'True'
					elif obj[11]>1:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=3:
							return 'False'
						elif obj[5]>3:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Occupation", "instances": 34, "metric_value": 0.7871, "depth": 2}
		if obj[6]<=10:
			# {"feature": "Coupon", "instances": 28, "metric_value": 0.5917, "depth": 3}
			if obj[2]>1:
				# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.2762, "depth": 4}
				if obj[8]>1.0:
					return 'True'
				elif obj[8]<=1.0:
					# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]>2:
						return 'True'
					elif obj[1]<=2:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>1:
							return 'False'
						elif obj[4]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=1:
				# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[4]>2:
					# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=0.0:
						return 'False'
					elif obj[7]>0.0:
						# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[8]<=0.0:
							return 'True'
						elif obj[8]>0.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]>10:
			# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[1]>2:
				return 'False'
			elif obj[1]<=2:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'True'
