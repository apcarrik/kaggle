def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[3]>1:
		# {"feature": "Children", "instances": 61, "metric_value": 0.9127, "depth": 2}
		if obj[7]>0:
			# {"feature": "Income", "instances": 31, "metric_value": 0.6374, "depth": 3}
			if obj[10]>1:
				# {"feature": "Time", "instances": 23, "metric_value": 0.4262, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[9]<=4:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[15]<=2:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[14]<=0:
								return 'False'
							elif obj[14]>0:
								return 'True'
							else: return 'True'
						elif obj[15]>2:
							return 'True'
						else: return 'True'
					elif obj[9]>4:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[10]<=1:
				# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[11]<=1.0:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[15]>1:
						return 'False'
					elif obj[15]<=1:
						return 'True'
					else: return 'True'
				elif obj[11]>1.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[7]<=0:
			# {"feature": "Coupon_validity", "instances": 30, "metric_value": 1.0, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Occupation", "instances": 18, "metric_value": 0.8524, "depth": 4}
				if obj[9]>1:
					# {"feature": "Distance", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[15]>1:
						return 'True'
					elif obj[15]<=1:
						# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=0:
									return 'False'
								elif obj[1]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]<=1:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[8]>0:
						return 'False'
					elif obj[8]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>0:
				# {"feature": "Passanger", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>0:
						return 'True'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Distance", "instances": 24, "metric_value": 0.9544, "depth": 2}
		if obj[15]>1:
			# {"feature": "Bar", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[11]<=2.0:
				# {"feature": "Age", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[6]>0:
					return 'False'
				elif obj[6]<=0:
					# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=0:
						return 'True'
					elif obj[4]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[11]>2.0:
				return 'True'
			else: return 'True'
		elif obj[15]<=1:
			# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[2]<=0:
				return 'True'
			elif obj[2]>0:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'False'
