def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[3]>1:
		# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.9629, "depth": 2}
		if obj[7]<=2.0:
			# {"feature": "Bar", "instances": 19, "metric_value": 0.998, "depth": 3}
			if obj[6]<=1.0:
				# {"feature": "Passanger", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[5]<=7:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[5]>7:
						# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=2:
							return 'False'
						elif obj[4]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			elif obj[6]>1.0:
				return 'False'
			else: return 'False'
		elif obj[7]>2.0:
			# {"feature": "Passanger", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[1]>3:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=3:
						return 'False'
					elif obj[2]>3:
						return 'True'
					else: return 'True'
				elif obj[1]<=3:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[5]>0:
			# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.7425, "depth": 3}
			if obj[7]<=3.0:
				# {"feature": "Bar", "instances": 15, "metric_value": 0.5665, "depth": 4}
				if obj[6]<=1.0:
					return 'False'
				elif obj[6]>1.0:
					# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[1]>0:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[4]<=2:
							return 'False'
						elif obj[4]>2:
							# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=2:
								return 'False'
							elif obj[2]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]>3.0:
				# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[10]>1:
					return 'True'
				elif obj[10]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[5]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
