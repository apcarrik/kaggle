def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[4]<=21:
		# {"feature": "Passanger", "instances": 31, "metric_value": 0.9072, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 18, "metric_value": 0.9911, "depth": 3}
			if obj[3]<=1:
				# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[1]>1:
					# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[9]>1:
						# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=2:
							return 'False'
						elif obj[2]>2:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0.0:
								return 'False'
							elif obj[5]>0.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[9]<=1:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			elif obj[3]>1:
				# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[6]<=1.0:
						return 'False'
					elif obj[6]>1.0:
						# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]>1.0:
							return 'False'
						elif obj[5]<=1.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>2:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[2]<=3:
				return 'True'
			elif obj[2]>3:
				# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[5]<=0.0:
						return 'True'
					elif obj[5]>0.0:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]>21:
		return 'False'
	else: return 'False'
