def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[3]>1:
		# {"feature": "Time", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[1]>0:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[2]>2:
				# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[5]<=0.0:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[0]<=2:
						return 'True'
					elif obj[0]>2:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=7:
							return 'True'
						elif obj[4]>7:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]>0.0:
					# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]>4:
						return 'False'
					elif obj[4]<=4:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[7]<=0:
							return 'False'
						elif obj[7]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=2:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[4]>0:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[6]<=1.0:
					return 'False'
				elif obj[6]>1.0:
					return 'True'
				else: return 'True'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]<=1:
		return 'True'
	else: return 'True'
