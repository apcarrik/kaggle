def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[4]>6:
			# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[7]>0.0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[7]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[2]>2:
				return 'True'
			else: return 'True'
		elif obj[4]<=6:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[9]<=2:
					return 'False'
				elif obj[9]>2:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]<=0:
						return 'False'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
