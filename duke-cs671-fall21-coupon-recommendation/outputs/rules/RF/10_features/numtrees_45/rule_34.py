def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[4]>1:
		# {"feature": "Time", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[1]>0:
			# {"feature": "Passanger", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[6]<=1.0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[3]<=3:
						return 'False'
					elif obj[3]>3:
						return 'True'
					else: return 'True'
				elif obj[6]>1.0:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=2:
						return 'True'
					elif obj[3]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[4]<=1:
		return 'False'
	else: return 'False'
