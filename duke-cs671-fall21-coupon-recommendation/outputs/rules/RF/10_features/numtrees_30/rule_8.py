def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[6]<=3.0:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[4]>1:
			# {"feature": "Distance", "instances": 28, "metric_value": 0.9963, "depth": 3}
			if obj[9]>1:
				# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[7]<=1.0:
					# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[1]>0:
						# {"feature": "Direction_same", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[8]<=0:
							return 'False'
						elif obj[8]>0:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[7]>1.0:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]<=3:
						return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]<=1:
				# {"feature": "Direction_same", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[8]<=0:
					return 'True'
				elif obj[8]>0:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]>1:
						return 'False'
					elif obj[2]<=1:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[4]<=1:
			return 'True'
		else: return 'True'
	elif obj[6]>3.0:
		return 'False'
	else: return 'False'
