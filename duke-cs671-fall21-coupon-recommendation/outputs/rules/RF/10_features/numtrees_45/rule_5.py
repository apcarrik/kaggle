def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[4]<=9:
		# {"feature": "Passanger", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[3]<=1:
				# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]<=1:
						return 'True'
					elif obj[2]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]>1:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]>3:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]<=3:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[4]>9:
		# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
