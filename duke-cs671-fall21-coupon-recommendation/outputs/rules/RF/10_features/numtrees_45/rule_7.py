def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.8113, "depth": 2}
		if obj[6]>1.0:
			# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[3]<=2:
				return 'True'
			elif obj[3]>2:
				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[4]<=1:
					return 'False'
				elif obj[4]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]<=1.0:
			# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>0:
					# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>4:
						return 'False'
					elif obj[4]<=4:
						return 'True'
					else: return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 2}
		if obj[7]<=1.0:
			return 'False'
		elif obj[7]>1.0:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
