def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[6]>0:
		# {"feature": "Distance", "instances": 21, "metric_value": 0.8631, "depth": 2}
		if obj[12]>1:
			# {"feature": "Passanger", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[2]>2:
					return 'True'
				elif obj[2]<=2:
					# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[7]>4:
							return 'False'
						elif obj[7]<=4:
							return 'True'
						else: return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]>1:
				# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[4]<=3:
					return 'False'
				elif obj[4]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[12]<=1:
			return 'True'
		else: return 'True'
	elif obj[6]<=0:
		# {"feature": "Bar", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[8]>0.0:
			# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[8]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'False'
