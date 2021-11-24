def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[2]>0:
		# {"feature": "Distance", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[9]<=1:
			# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[0]<=2:
				return 'True'
			elif obj[0]>2:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]>1:
			# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[6]>1.0:
				# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[8]<=0:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]<=2:
						return 'True'
					elif obj[3]>2:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'True'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[8]>0:
					return 'False'
				else: return 'False'
			elif obj[6]<=1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
