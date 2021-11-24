def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[4]<=7:
		# {"feature": "Bar", "instances": 25, "metric_value": 0.8555, "depth": 2}
		if obj[5]<=1.0:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]>1.0:
			# {"feature": "Passanger", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[6]>2.0:
					# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=3:
							return 'False'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[6]<=2.0:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]>7:
		# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[6]<=2.0:
			return 'False'
		elif obj[6]>2.0:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[3]>1:
				return 'True'
			elif obj[3]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
