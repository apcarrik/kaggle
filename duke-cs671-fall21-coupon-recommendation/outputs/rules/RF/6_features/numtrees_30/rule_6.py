def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[3]<=16:
		# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 1.0, "depth": 2}
		if obj[4]<=2.0:
			# {"feature": "Passanger", "instances": 24, "metric_value": 0.9799, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 18, "metric_value": 1.0, "depth": 4}
				if obj[2]>1:
					# {"feature": "Distance", "instances": 15, "metric_value": 0.971, "depth": 5}
					if obj[5]>1:
						# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[1]<=2:
							return 'False'
						elif obj[1]>2:
							return 'True'
						else: return 'True'
					elif obj[5]<=1:
						# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[1]<=3:
							return 'True'
						elif obj[1]>3:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>2.0:
			return 'False'
		else: return 'False'
	elif obj[3]>16:
		return 'False'
	else: return 'False'
