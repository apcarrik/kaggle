def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[9]>0.0:
		# {"feature": "Bar", "instances": 71, "metric_value": 0.9757, "depth": 2}
		if obj[7]>0.0:
			# {"feature": "Age", "instances": 39, "metric_value": 0.8582, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Coffeehouse", "instances": 20, "metric_value": 1.0, "depth": 4}
				if obj[8]<=2.0:
					# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[6]<=10:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>10:
						# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[1]<=0:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=2:
								return 'True'
							elif obj[2]>2:
								return 'False'
							else: return 'False'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[8]>2.0:
					# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[1]>1:
						# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[10]>0:
							return 'False'
						elif obj[10]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]>2:
				# {"feature": "Time", "instances": 19, "metric_value": 0.2975, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[5]<=2:
						return 'True'
					elif obj[5]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[7]<=0.0:
			# {"feature": "Passanger", "instances": 32, "metric_value": 0.9887, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Distance", "instances": 24, "metric_value": 0.9183, "depth": 4}
				if obj[11]>1:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[2]>2:
						return 'False'
					elif obj[2]<=2:
						# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[5]>1:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=1:
								return 'True'
							elif obj[1]>1:
								return 'False'
							else: return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[11]<=1:
					# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[6]<=8:
							return 'True'
						elif obj[6]>8:
							return 'False'
						else: return 'False'
					elif obj[1]>1:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=3:
							return 'False'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=2:
						return 'False'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[9]<=0.0:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[6]>6:
			# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[4]>1:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[4]<=1:
				return 'True'
			else: return 'True'
		elif obj[6]<=6:
			return 'False'
		else: return 'False'
	else: return 'False'
