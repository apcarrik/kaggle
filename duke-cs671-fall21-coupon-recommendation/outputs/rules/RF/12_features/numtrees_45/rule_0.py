def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Bar", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[7]<=1.0:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[5]<=2:
				# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[2]>0:
					# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]>1:
						# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[10]<=0:
							return 'False'
						elif obj[10]>0:
							return 'True'
						else: return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			elif obj[5]>2:
				return 'True'
			else: return 'True'
		elif obj[7]>1.0:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[6]>2:
			return 'True'
		elif obj[6]<=2:
			# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[4]<=2:
				return 'False'
			elif obj[4]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
