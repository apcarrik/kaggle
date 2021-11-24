def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[8]<=2.0:
		# {"feature": "Direction_same", "instances": 32, "metric_value": 1.0, "depth": 2}
		if obj[9]<=0:
			# {"feature": "Passanger", "instances": 30, "metric_value": 0.9968, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Coupon", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Education", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[7]<=2.0:
							return 'True'
						elif obj[7]>2.0:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=4:
								return 'False'
							elif obj[3]>4:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>2:
						# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[1]<=3:
							return 'False'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=6:
					# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[3]<=4:
						# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[7]>0.0:
							return 'False'
						elif obj[7]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[3]>4:
						return 'True'
					else: return 'True'
				elif obj[5]>6:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[9]>0:
			return 'True'
		else: return 'True'
	elif obj[8]>2.0:
		return 'True'
	else: return 'True'
