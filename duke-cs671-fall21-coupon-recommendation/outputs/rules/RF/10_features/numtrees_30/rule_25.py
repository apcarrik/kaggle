def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.8338, "depth": 1}
	if obj[9]<=2:
		# {"feature": "Education", "instances": 31, "metric_value": 0.7088, "depth": 2}
		if obj[3]>0:
			# {"feature": "Passanger", "instances": 20, "metric_value": 0.8813, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Time", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[1]>1:
					# {"feature": "Coupon", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[2]>1:
						return 'True'
					elif obj[2]<=1:
						# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[4]>2:
							return 'True'
						elif obj[4]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=1:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]>2:
						return 'False'
					elif obj[2]<=2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[3]<=0:
			return 'True'
		else: return 'True'
	elif obj[9]>2:
		return 'False'
	else: return 'False'
