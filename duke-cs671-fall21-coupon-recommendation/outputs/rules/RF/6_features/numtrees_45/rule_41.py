def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]<=14:
		# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Education", "instances": 16, "metric_value": 0.8113, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[1]>1:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=2:
							return 'True'
						elif obj[5]>2:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[4]>1.0:
			# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[5]<=2:
				return 'True'
			elif obj[5]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]>14:
		return 'True'
	else: return 'True'
