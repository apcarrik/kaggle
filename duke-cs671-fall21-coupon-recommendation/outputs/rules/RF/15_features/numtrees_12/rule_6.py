def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon_validity", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[3]<=0:
		# {"feature": "Coupon", "instances": 48, "metric_value": 0.896, "depth": 2}
		if obj[2]>1:
			# {"feature": "Time", "instances": 29, "metric_value": 0.5788, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Direction_same", "instances": 16, "metric_value": 0.8113, "depth": 4}
				if obj[13]<=0:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[8]<=8:
						# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[5]>0:
							return 'True'
						elif obj[5]<=0:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]>0:
								return 'False'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[8]>8:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[13]>0:
					return 'True'
				else: return 'True'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.9819, "depth": 3}
			if obj[8]>1:
				# {"feature": "Time", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[5]<=4:
						# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[11]<=2.0:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[12]>0.0:
								return 'True'
							elif obj[12]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[11]>2.0:
							return 'False'
						else: return 'False'
					elif obj[5]>4:
						return 'False'
					else: return 'False'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[8]<=1:
				# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[3]>0:
		# {"feature": "Time", "instances": 37, "metric_value": 0.974, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.7425, "depth": 3}
			if obj[8]<=6:
				# {"feature": "Passanger", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5]<=3:
						return 'False'
					elif obj[5]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[8]>6:
				# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[13]<=0:
					# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>0:
						return 'False'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				elif obj[13]>0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]>1:
			# {"feature": "Distance", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[14]>1:
				# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[12]<=1.0:
					# {"feature": "Gender", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[4]<=0:
						return 'False'
					elif obj[4]>0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=0:
								return 'True'
							elif obj[6]>0:
								return 'False'
							else: return 'False'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[12]>1.0:
					return 'True'
				else: return 'True'
			elif obj[14]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
