def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[8]>0.0:
		# {"feature": "Coupon", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[2]>2:
			# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[1]>0:
				# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>4:
						return 'False'
					elif obj[3]<=4:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]<=2:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[5]>1:
				# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=3:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=0:
							return 'False'
						elif obj[1]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]>3:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[5]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[8]<=0.0:
		return 'False'
	else: return 'False'
