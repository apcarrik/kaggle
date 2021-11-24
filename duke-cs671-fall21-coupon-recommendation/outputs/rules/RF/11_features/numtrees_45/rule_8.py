def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[3]<=4:
		# {"feature": "Passanger", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[2]>1:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[5]<=16:
					return 'False'
				elif obj[5]>16:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[6]<=1.0:
					# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[7]<=2.0:
						return 'False'
					elif obj[7]>2.0:
						return 'True'
					else: return 'True'
				elif obj[6]>1.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[5]<=10:
				return 'True'
			elif obj[5]>10:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]>4:
		return 'False'
	else: return 'False'
