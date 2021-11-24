def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[4]>4:
		# {"feature": "Education", "instances": 27, "metric_value": 0.951, "depth": 2}
		if obj[3]>0:
			# {"feature": "Bar", "instances": 19, "metric_value": 0.8315, "depth": 3}
			if obj[5]>1.0:
				# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[9]>2:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=2:
							return 'False'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[9]<=2:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[5]<=1.0:
				return 'False'
			else: return 'False'
		elif obj[3]<=0:
			# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[9]>1:
				# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1]>0:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]>0.0:
						return 'False'
					elif obj[7]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[9]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]<=4:
		# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[2]>1:
			return 'True'
		elif obj[2]<=1:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]<=0:
				return 'True'
			elif obj[0]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
