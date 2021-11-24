def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[7]>1.0:
		# {"feature": "Time", "instances": 13, "metric_value": 0.9612, "depth": 2}
		if obj[1]>1:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>4:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[3]<=4:
					return 'False'
				else: return 'False'
			elif obj[2]>2:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[4]>0:
				return 'False'
			elif obj[4]<=0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[7]<=1.0:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[5]<=7:
			return 'True'
		elif obj[5]>7:
			# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
