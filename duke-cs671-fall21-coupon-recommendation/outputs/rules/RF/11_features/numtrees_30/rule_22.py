def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 28, "metric_value": 0.9059, "depth": 2}
		if obj[5]>4:
			# {"feature": "Coffeehouse", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[7]>0.0:
				# {"feature": "Education", "instances": 19, "metric_value": 0.9495, "depth": 4}
				if obj[4]>1:
					# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[1]>1:
						# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[3]>2:
							# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>0.0:
								return 'False'
							elif obj[6]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[3]<=2:
							return 'True'
						else: return 'True'
					elif obj[1]<=1:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[10]>1:
							return 'False'
						elif obj[10]<=1:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[4]<=1:
					# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[7]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[5]<=4:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		return 'False'
	else: return 'False'
